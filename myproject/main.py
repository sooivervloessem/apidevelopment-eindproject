from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

import auth
import os
import crud
import models
import schemas
from database import SessionLocal, engine

print("We are in the main.......")
if not os.path.exists('.\sqlitedb'):
    print("Making folder.......")
    os.makedirs('.\sqlitedb')

print("Creating tables.......")
models.Base.metadata.create_all(bind=engine)
print("Tables created.......")

app = FastAPI()

origins = [
    "http://localhost:8000/",
    "https://sooivervloessem-kpop-api.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    # Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/listener/{listener_id}/{song_id}", response_model=schemas.ListenerSong)
def link_listener_song(listener_song: schemas.ListenerSongCreate, listener_id: int, song_id: int, db: Session = Depends(get_db)):
    return crud.create_user_song(db, listener_song=listener_song, listener_id=listener_id, song_id=song_id)


@app.post("/kpop_groups/", response_model=schemas.KpopGroup)
def create_kpop_group(kpop_group: schemas.KpopGroupCreate, db: Session = Depends(get_db)):
    return crud.create_kpop_group(db=db, kpop_group=kpop_group)


@app.get("/kpop_groups/", response_model=list[schemas.KpopGroup])
def read_kpop_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    kpop_groups = crud.get_kpop_groups(db, skip=skip, limit=limit)
    return kpop_groups


@app.get("/kpop_groups/{kpop_group_id}", response_model=schemas.KpopGroup)
def read_kpop_group(kpop_group_id: int, db: Session = Depends(get_db)):
    db_kpop_group = crud.get_kpop_group(db, kpop_group_id=kpop_group_id)
    if db_kpop_group is None:
        raise HTTPException(status_code=404, detail="Kpop group not found")
    return db_kpop_group


@app.post("/kpop_groups/{kpop_group_id}/songs/", response_model=schemas.Song)
def create_song_for_kpop_group(kpop_group_id: int, song: schemas.SongCreate, db: Session = Depends(get_db)):
    return crud.create_song_kpopgroup(db=db, song=song, kpop_group_id=kpop_group_id)


@app.get("/songs/", response_model=list[schemas.Song])
def read_songs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    songs = crud.get_songs(db, skip=skip, limit=limit)
    return songs


@app.get("/songs/{song_id}", response_model=schemas.Song)
def read_song(song_id: int, db: Session = Depends(get_db)):
    db_song = crud.get_songs_by_id(db, song_id=song_id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return db_song


@app.put("/songs/{song_id}", response_model=schemas.Song)
def update_song(song_id: int, song: schemas.SongCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.update_song_kpopgroup(db=db, song=song, song_id=song_id)


@app.delete("/songs/{song_id}")
def delete_song(song_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.delete_song_kpopgroup(db=db, song_id=song_id)

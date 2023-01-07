from sqlalchemy.orm import Session

import auth
import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Link listener to song
def create_user_song(db: Session, listener_song: schemas.ListenerSongCreate, listener_id: int, song_id: int):
    db_user_song = models.ListenerSong(**listener_song.dict(), listener_id=listener_id, song_id=song_id)
    db.add(db_user_song)
    db.commit()
    db.refresh(db_user_song)
    return db_user_song


def get_songs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Song).offset(skip).limit(limit).all()


def get_songs_by_id(db: Session, song_id: int):
    return db.query(models.Song).filter(models.Song.id == song_id).first()


def create_song_kpopgroup(db: Session, song: schemas.SongCreate, kpop_group_id: int):
    db_song = models.Song(**song.dict(), kpop_group_id=kpop_group_id)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


def get_kpop_group(db: Session, kpop_group_id: int):
    return db.query(models.KpopGroup).filter(models.KpopGroup.id == kpop_group_id).first()


def get_kpop_group_by_name(db: Session, name: str):
    return db.query(models.KpopGroup).filter(models.KpopGroup.name == name).first()


def get_kpop_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.KpopGroup).offset(skip).limit(limit).all()


def create_kpop_group(db: Session, kpop_group: schemas.KpopGroupCreate):
    db_kpop_group = models.KpopGroup(**kpop_group.dict())
    db.add(db_kpop_group)
    db.commit()
    db.refresh(db_kpop_group)
    return db_kpop_group


def update_song_kpopgroup(db: Session, song: schemas.SongCreate, song_id: int):
    db_song = db.get(models.Song, song_id)
    song_data = song.dict(exclude_unset=True)
    for key, value in song_data.items():
        setattr(db_song, key, value)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


def delete_song_kpopgroup(db: Session, song_id: int):
    db_song = db.get(models.Song, song_id)
    db.delete(db_song)
    db.commit()
    return {"Song deleted": True}

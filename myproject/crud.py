from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_songs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Song).offset(skip).limit(limit).all()


def create_user_song_kpopgroup(db: Session, song: schemas.SongCreate, user_id: int, kpop_group_id: int):
    db_song = models.Song(**song.dict(), listener_id=user_id, kpop_group_id=kpop_group_id)
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

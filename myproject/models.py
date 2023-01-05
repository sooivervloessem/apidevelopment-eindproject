from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    songs = relationship("ListenerSong", back_populates="listeners")


class ListenerSong(Base):
    __tablename__ = "listener_songs"

    id = Column(Integer, primary_key=True, index=True)
    listener_id = Column(Integer, ForeignKey("users.id"))
    song_id = Column(Integer, ForeignKey("songs.id"))

    listeners = relationship("User", back_populates="songs")
    songs = relationship("Song", back_populates="listeners")


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String, index=True)
    album = Column(String, index=True)
    release_date = Column(String, index=True)
    kpop_group_id = Column(Integer, ForeignKey("kpop_groups.id"))

    listeners = relationship("ListenerSong", back_populates="songs")
    kpop_group = relationship("KpopGroup", back_populates="songs")


class KpopGroup(Base):
    __tablename__ = "kpop_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    songs = relationship("Song", back_populates="kpop_group")

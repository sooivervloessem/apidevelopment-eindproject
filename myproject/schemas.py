from pydantic import BaseModel


class ListenerSongBase(BaseModel):
    pass


class ListenerSongCreate(ListenerSongBase):
    pass


class ListenerSong(ListenerSongBase):
    id: int
    listener_id: int
    song_id: int

    class Config:
        orm_mode = True


class SongBase(BaseModel):
    title: str
    artist: str
    album: str | None = None
    release_date: str | None = None


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: int
    kpop_group_id: int

    listeners: list[ListenerSong] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    songs: list[ListenerSong] = []

    class Config:
        orm_mode = True


class KpopGroupBase(BaseModel):
    name: str


class KpopGroupCreate(KpopGroupBase):
    pass


class KpopGroup(KpopGroupBase):
    id: int
    songs: list[Song] = []

    class Config:
        orm_mode = True

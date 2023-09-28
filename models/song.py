import uuid

from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.orm import relationship

from .base import Base


class Song(Base):
    __tablename__ = 'song'

    id = Column("id", String(36), primary_key=True)
    spotify_id = Column(String(64), nullable=False)
    title = Column(String(128), nullable=False)
    duration = Column(Integer, nullable=False)
    artist = Column(String(128), nullable=False)
    album = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime)
    playlists = relationship('Playlist', secondary='playlist_song', back_populates='songs')

    def __init__(self, spotify_id:str, title:str, duration:int, artist:str, album:str):
        self.id = str(uuid.uuid4())
        self.spotify_id = spotify_id
        self.title = title
        self.duration = duration
        self.artist = artist
        self.album = album

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

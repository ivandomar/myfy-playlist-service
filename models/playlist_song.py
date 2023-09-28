from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, String

from .base import Base


class PlaylistSong(Base):
    __tablename__ = 'playlist_song'

    playlist_id = Column(String(36), ForeignKey("playlist.id"), primary_key=True)
    song_id = Column(String(36), ForeignKey("song.id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __init__(self, playlist_id:str, song_id: str):
        self.playlist_id = playlist_id
        self.song_id = song_id

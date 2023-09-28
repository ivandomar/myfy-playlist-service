import uuid

from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, String, relationship
from constants import token

from .base import Base


class Playlist(Base):
    __tablename__ = 'playlist'

    id = Column("id", String(36), primary_key=True)
    user_id = Column(String(36), ForeignKey("user.id"), nullable=False)
    title = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(), nullable=False)
    deleted_at = Column(DateTime)
    songs = relationship('Song', secondary='playlist_song', back_populates='playlists')

    def __init__(self, user_id:str, title: str):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.title = title

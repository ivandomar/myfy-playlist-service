from datetime import datetime
from pydantic import BaseModel
from typing import List


class SongResponseSchema(BaseModel):
    id: str
    spotify_id: str
    title: str
    duration: int
    artist: str
    album: str
    created_at: str
    updated_at: str

class SpotifyResponseSchema(BaseModel):
    spotify_id: str
    title: str
    duration: int
    artist: str
    album: str

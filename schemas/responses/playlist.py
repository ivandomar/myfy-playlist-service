from datetime import datetime
from pydantic import BaseModel
from typing import List
from .song import SongResponseSchema


class PlaylistResponseSchema(BaseModel):
    id: str
    title: str
    created_at: str
    updated_at: str
    songs: List[SongResponseSchema]

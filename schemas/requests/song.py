from pydantic import BaseModel


class AddSongRequestSchema(BaseModel):
    spotify_id: str

class AddSongPathRequestSchema(BaseModel):
    user_id: str
    token: str
    playlist_id: str

class RemoveSongRequestSchema(BaseModel):
    id: str
    playlist_id: str
    user_id: str
    token: str

class SearchSongRequestSchema(BaseModel):
    term: str

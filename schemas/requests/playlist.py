from pydantic import BaseModel


class CreatePlaylistRequestSchema(BaseModel):
    title: str

class CreatePlaylistPathRequestSchema(BaseModel):
    user_id: str
    token: str 

class RemovePlaylistRequestSchema(BaseModel):
    id: str
    user_id: str
    token: str

class UpdatePlaylistPathRequestSchema(BaseModel):
    id: str
    user_id: str
    token: str

class UpdatePlaylistBodyRequestSchema(BaseModel):
    title: str

class GetPlaylistRequestSchema(BaseModel):
    id: str
    user_id: str
    token: str

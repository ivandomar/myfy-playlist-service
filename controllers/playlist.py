import hashlib

from constants.error_messages import INVALID_TOKEN, DUPLICATED_ELEMENT, GENERAL_ERROR, NOT_FOUND
from constants.http_statuses import CREATED, OK, SEMANTIC_ERROR, SYNTAX_ERROR
from database import Session
from datetime import datetime
from flask import request
from formatters.playlist import format_playlist_response
from models import Playlist, Song, PlaylistSong
from schemas.requests.playlist import CreatePlaylistPathRequestSchema, CreatePlaylistRequestSchema, RemovePlaylistRequestSchema, UpdatePlaylistBodyRequestSchema, UpdatePlaylistPathRequestSchema, GetPlaylistRequestSchema
from sqlalchemy import or_


def get(path: GetPlaylistRequestSchema):
    id = path.id
    user_id = path.user_id
    token = path.token
    
    try:
        session = Session()

        playlist = session.query(Playlist).filter(
            Playlist.id == id,
            Playlist.deleted_at == None
        ).one_or_none()

        if playlist is None:
            raise ValueError(NOT_FOUND)

        session.close()

        return format_playlist_response(playlist), OK
        
    except ValueError as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR
    except Exception as e:        
        return {"mesage": str(e)}, SYNTAX_ERROR
    

def create(path: CreatePlaylistPathRequestSchema, body: CreatePlaylistRequestSchema):
    new_playlist = Playlist(path.user_id, body.title)

    try:
        session = Session()

        session.add(new_playlist)
        session.commit()
        session.close()
        
        return format_playlist_response(new_playlist), CREATED
    except Exception as e:
        return {"message": GENERAL_ERROR}, SYNTAX_ERROR
    

def delete(path: RemovePlaylistRequestSchema):
    id = path.id
    user_id = path.user_id
    token = path.token

    try:
        session = Session()
        session.query(Playlist).filter(Playlist.id == id).update({'deleted_at': datetime.now()})
        session.commit()
        session.close()
        
        return '', OK

    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR


def update(path: UpdatePlaylistPathRequestSchema, body: UpdatePlaylistBodyRequestSchema):
    id = path.id
    user_id = path.user_id
    token = path.token
        
    try:
        session = Session()

        playlist = session.query(Playlist).filter(Playlist.id == id).one_or_none()

        if playlist is None:
            raise ValueError(NOT_FOUND)

        new_title = body.title or playlist.name
        
        new_data = {
            'title': new_title,
            'updated_at': datetime.now()
        }

        session.query(Playlist).filter(Playlist.id == id).update(new_data)

        updated_playlist = session.query(Playlist).filter(Playlist.id == id).one_or_none()

        session.commit()
        session.close()
        
        return format_playlist_response(updated_playlist), OK

    except ValueError as e:
        return {"mesage": str(e)}, SEMANTIC_ERROR
    except Exception as e:        
        return {"mesage": GENERAL_ERROR}, SYNTAX_ERROR

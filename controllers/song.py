import hashlib

from constants.error_messages import INVALID_TOKEN, DUPLICATED_ELEMENT, GENERAL_ERROR, NOT_FOUND
from constants.http_statuses import CREATED, OK, SEMANTIC_ERROR, SYNTAX_ERROR
from database import Session
from datetime import datetime
from flask import request
from formatters.playlist import format_playlist_response
from models import Playlist, Song
from schemas.requests.song import AddSongPathRequestSchema, AddSongRequestSchema, RemoveSongRequestSchema
from sqlalchemy import or_    

def add(path: AddSongPathRequestSchema, body: AddSongRequestSchema):
    playlist_id = path.playlist_id
    user_id = path.user_id
    token = path.token

    new_song = Song(body.spotify_id, 'title', 0, 'artist', 'album')
    try:
        session = Session()

        playlist = session.query(Playlist).filter(
            Playlist.id == playlist_id,
            Playlist.deleted_at == None
        ).one_or_none()

        if playlist is None:
            raise AttributeError(NOT_FOUND)
        
        playlist.songs.append(new_song)

        session.commit()
        session.close()
        
        return format_playlist_response(playlist), CREATED
    except AttributeError as e:
        return {"message": str(e)}, SEMANTIC_ERROR
    except Exception as e:
        return {"message": GENERAL_ERROR}, SYNTAX_ERROR
    

def remove(path: RemoveSongRequestSchema):
    id = path.id
    playlist_id = path.playlist_id
    user_id = path.user_id
    token = path.token

    try:
        session = Session()

        playlist = session.query(Playlist).filter(
            Playlist.id == playlist_id,
            Playlist.deleted_at == None
        ).one_or_none()

        if playlist is None:
            raise AttributeError(NOT_FOUND)
        
        matching_song = None
        for song in playlist.songs:
            if song.id == id:
                matching_song = song

        if matching_song is None:
            raise AttributeError(NOT_FOUND)
        
        playlist.songs.remove(matching_song)

        session.commit()
        session.close()
        
        return format_playlist_response(playlist), CREATED
    except AttributeError as e:
        return {"message": str(e)}, SEMANTIC_ERROR
    except Exception as e:
        return {"message": GENERAL_ERROR}, SYNTAX_ERROR

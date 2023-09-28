from formatters.song import format_song_response
from models import Playlist, Song
from typing import List

def format_playlist_response(playlist: Playlist, songs: List[Song]):
    formatted_songs = []

    for song in songs:
        formatted_songs.append(format_song_response(song))

    return {
        'id': playlist.id,
        'title': playlist.title,
        'created_at': playlist.created_at,
        'updated_at': playlist.updated_at,
        'songs': formatted_songs
    }
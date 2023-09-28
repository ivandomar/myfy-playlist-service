from models.song import Song

def format_song_response(song: Song):
    return {
        'id': song.id,
        'spotify_id': song.spotify_id,
        'title': song.title,
        'duration': song,
        'artist': song.artist,
        'album': song.album,
        'created_at': song.created_at,
        'updated_at': song.updated_at
    }
from flask_openapi3 import APIBlueprint, Tag

from constants.http_statuses import OK, SEMANTIC_ERROR, SYNTAX_ERROR
from controllers.song import search
from schemas.responses.song import SpotifyResponseSchema
from schemas.responses.general import ErrorResponseSchema

song_blueprint = APIBlueprint("song", __name__, url_prefix="/song")

song_tag = Tag(name="Song", description="Spotify song search endpoints")

song_blueprint.get(
    '/spotify/<term>',
    tags=[song_tag],
    summary='Searches for term in Spotify songs',
    responses={
        str(OK): SpotifyResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(search)

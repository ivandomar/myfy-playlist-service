from flask_openapi3 import APIBlueprint, Tag

from constants.http_statuses import OK, SEMANTIC_ERROR, SYNTAX_ERROR
from controllers.playlist import create, delete, get, update
from controllers.song import add, remove
from schemas.responses.playlist import PlaylistResponseSchema
from schemas.responses.general import ErrorResponseSchema

playlist_blueprint = APIBlueprint("playlist", __name__, url_prefix="/playlist")

playlist_tag = Tag(name="Playlist", description="Playlist management endpoints")

playlist_blueprint.post(
    '/user/<user_id>/token/<token>',
    tags=[playlist_tag],
    summary='Creates new playlist',
    responses={
        str(OK): PlaylistResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(create)

playlist_blueprint.delete(
    '/user/<user_id>/token/<token>/<id>',
    tags=[playlist_tag],
    summary='Removes specified playlist',
    responses={
        str(OK): None,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(delete)

playlist_blueprint.get(
    '/user/<user_id>/token/<token>/<id>',
    tags=[playlist_tag],
    summary='Gets specified playlist',
    responses={
        str(OK): PlaylistResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(get)

playlist_blueprint.put(
    '/user/<user_id>/token/<token>/<id>',
    tags=[playlist_tag],
    summary='Updates title of specified playlist',
    responses={
        str(OK): PlaylistResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(update)

playlist_blueprint.post(
    '/<playlist_id>/user/<user_id>/token/<token>/song',
    tags=[playlist_tag],
    summary='Adds song to specified playlist',
    responses={
        str(OK): PlaylistResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(add)

playlist_blueprint.delete(
    '/<playlist_id>/user/<user_id>/token/<token>/song/<id>',
    tags=[playlist_tag],
    summary='Removes song from specified playlist',
    responses={
        str(OK): PlaylistResponseSchema,
        str(SEMANTIC_ERROR): ErrorResponseSchema,
        str(SYNTAX_ERROR): ErrorResponseSchema
        }
)(remove)

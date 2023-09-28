from flask_openapi3 import APIBlueprint, Tag

from controllers.home import index

home_tag = Tag(name="Documentation", description="Documentation suite")

main_blueprint = APIBlueprint("main", __name__)

main_blueprint.get("/", tags=[home_tag], summary="Renders Swagger API docs")(index)

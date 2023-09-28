from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info
from urllib.parse import unquote

import database

from routes.main import main_blueprint
from routes.auth import auth_blueprint
from routes.user import user_blueprint

info = Info(title="myfy auth service", version="0.0.1")
app = OpenAPI(__name__, info=info)

CORS(app)

app.register_api(main_blueprint)
app.register_api(auth_blueprint)
app.register_api(user_blueprint)

# Simple, one file Flask App
from flask import Flask
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from apps.core import routers
from apps.core.database import alchemy
from apps.core.database.configuration import get_postgresql_url
from settings import get_settings

def register_routers(app: Flask) -> Flask:

    app.register_api(routers.api)
    return app

def create_app(settings):
    info = Info(title="book API", version="1.0.0")
    app = OpenAPI(__name__, info=info)
    app.config["SQLALCHEMY_DATABASE_URI"] = get_postgresql_url(settings)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    return app

def init_databases(app: Flask) -> Flask:
    alchemy.db.init_app(app)
    alchemy.migrate.init_app(
        app, alchemy.db, directory="apps/core/database/migrations"
    )
    return app

def init_app(settings):
    app = create_app(settings)
    register_routers(app)
    init_databases(app)
    return app


app = init_app(get_settings)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True,
        port=8000
    )

# Simple, one file Flask App
from flask import Flask
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from apps.company.infrastructure.rest import routers as company_routers
from apps.user.infrastructure.rest import routers as user_routers
from apps.project.infrastructure.rest import routers as project_routers
from apps.core.database import alchemy
from apps.core.database import models
from apps.core.database.configuration import get_postgresql_url
from settings import get_settings


def register_routers(app: Flask) -> Flask:

    app.register_api(company_routers.api)
    app.register_api(user_routers.api)
    app.register_api(project_routers.api)
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
        app, alchemy.db, directory="src/apps/core/database/migrations"
    )
    return app


def init_app(settings):
    app = create_app(settings)
    init_databases(app)
    register_routers(app)
    return app


app = init_app(get_settings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)

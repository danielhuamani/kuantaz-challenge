from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import DeclarativeMeta

db = SQLAlchemy()
migrate = Migrate()

BaseModel: DeclarativeMeta = db.Model

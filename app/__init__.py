import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

APP_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_PROJECT_DIR = os.path.abspath(os.path.join(APP_DIR, '..'))

db = SQLAlchemy()
migrate = Migrate()
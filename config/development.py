"""Development Flask config variabels."""
from .base import BaseConfig, environ_or_default

import logging


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = environ_or_default(environ_name='LOG_LEVEL', default=logging.INFO)
    SQLALCHEMY_DATABASE_URI = environ_or_default(environ_name='SQLALCHEMY_DATABASE_URI', default=None)

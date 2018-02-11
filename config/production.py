"""Production Flask config variabels."""
from .base import BaseConfig, enviorn_or_default
import logging


class ProductionConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = enviorn_or_default(environ_name='LOG_LEVEL', default=logging.WARN)
    SQLALCHEMY_DATABASE_URI = enviorn_or_default(environ_name='SQLALCHEMY_DATABASE_URI', default=None)

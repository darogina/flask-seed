"""Local Flask config variabels."""
from .base import BaseConfig, environ_or_default
from app import ROOT_PROJECT_DIR

import logging
import os


class LocalConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = environ_or_default(environ_name='LOG_LEVEL', default=logging.DEBUG)
    SQLALCHEMY_DATABASE_URI = environ_or_default(environ_name='SQLALCHEMY_DATABASE_URI',
                                                 default='sqlite:///%s' % (os.path.join(ROOT_PROJECT_DIR, 'dev.db')))
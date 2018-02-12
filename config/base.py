"""Base Flask config variabels."""

import logging

from .utils import environ_or_default


class BaseConfig:
    DEBUG = False
    testbool = environ_or_default(environ_name="TEST_BOOL", default=None, type_override=bool)
    LOG_LEVEL = environ_or_default(environ_name='LOG_LEVEL', default=logging.INFO)

    SECRET_KEY = environ_or_default(environ_name='SECRET_KEY', default='MY SECRET')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ_or_default(environ_name='SQLALCHEMY_TRACK_MODIFICATIONS', default=False,
                                                        type_override=bool)

    STATIC_FOLDER = None

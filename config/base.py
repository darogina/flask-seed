"""Base Flask config variabels."""

import logging

from .utils import enviorn_or_default


class BaseConfig:
    DEBUG = False
    testbool = enviorn_or_default(environ_name="TEST_BOOL", default=None, type_override=bool)
    LOG_LEVEL = enviorn_or_default(environ_name='LOG_LEVEL', default=logging.INFO)

    SECRET_KEY = enviorn_or_default(environ_name='SECRET_KEY', default='MY SECRET')
    SQLALCHEMY_TRACK_MODIFICATIONS = enviorn_or_default(environ_name='SQLALCHEMY_TRACK_MODIFICATIONS', default=False,
                                                        type_override=bool)

    STATIC_FOLDER = None

# class Test(BaseConfig):
#
#     """Test Flask config variabels."""
#
#     DEBUG = True
#     TESTING = True
#     PRESERVE_CONTEXT_ON_EXCEPTION = False
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
#     WTF_CSRF_ENABLED = False

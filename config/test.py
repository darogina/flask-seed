import os

from app import ROOT_PROJECT_DIR
from .base import BaseConfig

TEST_DB_NAME = 'test.db'
TEST_DB_PATH = os.path.join(ROOT_PROJECT_DIR, TEST_DB_NAME)


class TestConfig(BaseConfig):
    """Test Flask config variabels."""

    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % TEST_DB_PATH
    WTF_CSRF_ENABLED = False
    DISABLE_AUTH = True

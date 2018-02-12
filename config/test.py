from .base import BaseConfig
from app import ROOT_PROJECT_DIR

import os

TEST_DB_NAME = 'test.db'
TEST_DB_PATH = os.path.join(ROOT_PROJECT_DIR, TEST_DB_NAME)

class TestConfig(BaseConfig):
    """Test Flask config variabels."""

    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (TEST_DB_PATH)
    WTF_CSRF_ENABLED = False
    FORCE_DISABLE_AUTH = True

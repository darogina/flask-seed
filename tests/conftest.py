import os

import pytest
from flask_migrate import downgrade, upgrade

from app.app import create_app, db as _db, ROOT_PROJECT_DIR

ALEMBIC_CONFIG = os.path.abspath(os.path.join(ROOT_PROJECT_DIR, 'migrations/alembic.ini'))


def apply_migrations():
    """Applies all alembic migrations."""
    upgrade(revision="head", sql=False)


def remove_migrations():
    """Remove all alembic migrations."""
    downgrade(revision="base", sql=False)


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    app = create_app('test')

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""

    from config.test import TEST_DB_PATH
    if os.path.exists(TEST_DB_PATH):
        os.unlink(TEST_DB_PATH)
    if os.path.exists(TEST_DB_PATH + '-journal'):
        os.unlink(TEST_DB_PATH + '-journal')

    def teardown():
        remove_migrations()
        os.unlink(TEST_DB_PATH)

    _db.app = app
    _db.init_app(app)
    apply_migrations()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function', autouse=True)
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session

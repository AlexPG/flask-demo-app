import pytest

from demo_app import create_app
from demo_app import db as _db

@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()

    yield app

    app_context.pop()

@pytest.fixture(scope='session')
def app_client(app):
    client = app.test_client()

    return client

@pytest.fixture(scope='module')
def db():
    _db.create_all()

    yield _db

    _db.drop_all()

@pytest.fixture(scope='function')
def session(db):
    session = db.create_scoped_session()

    db.session = session

    yield  session

    session.remove()

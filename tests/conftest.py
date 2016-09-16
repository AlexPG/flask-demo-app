import pytest

from demo_app import create_app
from demo_app import db as _db

@pytest.fixture(scope='session')
def app(request):
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()

    def teardown():
        app_context.pop()

    request.addfinalizer(teardown)

    return app

@pytest.fixture(scope='session')
def app_client(app):
    client = app.test_client()

    return client

@pytest.fixture(scope='session')
def db(app, request):
    _db.create_all()

    def teardown():
        _db.drop_all()

    request.addfinalizer(teardown)

    return _db

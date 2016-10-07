import pytest

from demo_app import create_app
from demo_app import db as _db

from demo_app.blog.models import Author, Category

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

@pytest.fixture()
def create_authors(session):
    mike = Author(name='Mike', description="Hi, I'm Mike Doe", email='mike@example.com')
    jane = Author(name='Jane', description="Hi, I'm Jane Doe", email='jane@example.com')
    session.add_all([mike, jane])
    session.commit()

@pytest.fixture()
def create_categories(session):
    python = Category(name='Python')
    javascript = Category(name='Javascript')
    session.add_all([python, javascript])
    session.commit()

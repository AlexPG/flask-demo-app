import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from demo_app.blog.models import Author

# Author model
def test_author_can_post(app, session):
    author = Author(name='John', description='Hi, I am John Doe', \
                    email='john@example.com')
    session.add(author)
    session.commit()

def test_author_cant_post_same_user(app, session):
    author = Author(name='John', description='Hi, I am John Doe', \
                    email='john@example.com')
    session.add(author)
    with pytest.raises(IntegrityError):
        session.commit()

def test_author_can_post_another_author(app, session):
    author = Author(name='Jane', description='Hi, I am Jane Doe', \
                    email='jane@example.com')
    session.add(author)
    session.commit()

def test_author_can_get_existing_author(app, session):
    john = Author.query.filter_by(name='John').first()
    assert john.name == 'John'

def test_author_cant_get_non_existing_author(app, session):
    mike = Author.query.filter_by(name='Mike').first()
    assert mike == None

def test_author_can_get_existing_user_list(app, session):
    authors = Author.query.all()
    assert len(authors) > 0

def test_author_can_update_existing_user(app, session):
    author = Author.query.filter_by(name='John').first()
    author.email = 'mike@example.com'
    session.commit()

def test_author_cant_update_existing_user_with_non_unique_email(app, session):
    author = Author.query.filter_by(name='John').first()
    author.email = 'jane@example.com'
    with pytest.raises(IntegrityError):
        session.commit()

def test_author_can_delete_existing_user(app, session):
    author = Author.query.filter_by(name='John').first()
    session.delete(author)
    session.commit()

def test_author_cant_delete_non_existing_user(app, session):
    author = Author.query.filter_by(name='Mike').first()
    with pytest.raises(UnmappedInstanceError):
        session.delete(author)
        session.commit()

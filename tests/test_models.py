import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from demo_app.blog.models import Author, Category, Entry

# Author model
def test_author_can_post(app, session):
    author = Author(name='John', description='Hi, I am John Doe', \
                    email='john@example.com')
    session.add(author)
    session.commit()

def test_author_cant_post_same_author(app, session):
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

def test_author_can_get_existing_author_list(app, session):
    authors = Author.query.all()
    assert len(authors) > 0

def test_author_can_update_existing_author(app, session):
    author = Author.query.filter_by(name='John').first()
    author.email = 'mike@example.com'
    session.commit()

def test_author_cant_update_existing_author_with_non_unique_email(app, session):
    author = Author.query.filter_by(name='John').first()
    author.email = 'jane@example.com'
    with pytest.raises(IntegrityError):
        session.commit()

def test_author_can_delete_existing_author(app, session):
    author = Author.query.filter_by(name='John').first()
    session.delete(author)
    session.commit()

def test_author_cant_delete_non_existing_author(app, session):
    author = Author.query.filter_by(name='Mike').first()
    with pytest.raises(UnmappedInstanceError):
        session.delete(author)
        session.commit()

# Category model
def test_category_can_post(app, session):
    category = Category(name='IT')
    session.add(category)
    session.commit()

def test_category_cant_post_same_category(app, session):
    category = Category(name='IT')
    session.add(category)
    with pytest.raises(IntegrityError):
        session.commit()

def test_category_can_post_another_category(app, session):
    category = Category(name='Sport')
    session.add(category)
    session.commit()

def test_category_can_update_existing_category(app, session):
    category = Category.query.filter_by(name='IT').first()
    category.name = 'Flask'
    session.commit()

def test_category_cant_update_existing_category_with_non_unique_name(app, session):
    category = Category.query.filter_by(name='Flask').first()
    category.name = 'Sport'
    with pytest.raises(IntegrityError):
        session.commit()

def test_category_can_delete_existing_category(app, session):
    category = Category.query.filter_by(name='Flask').first()
    session.delete(category)
    session.commit()

def test_category_cant_delete_non_existing_category(app, session):
    category = Category.query.filter_by(name='Flask').first()
    with pytest.raises(UnmappedInstanceError):
        session.delete(category)
        session.commit()

# Entry model
def test_entry_can_post(app, session):
    john = Author(name='John', description='Hi, I am John Doe', \
                  email='john@example.com')
    session.add(john)
    session.commit()

    it = Category(name='IT')
    flask = Category(name='Flask')
    python = Category(name='Python')
    session.add_all([it, flask, python])
    session.commit()

    entry1 = Entry(title='Hello World', body='This is my first entry', \
                   author=john)
    entry1.en_ca.append(it)
    entry1.en_ca.append(python)
    session.add(entry1)

    jane = Author.query.filter_by(name='Jane').first()
    entry2 = Entry(title='Hello World', body='This is my second entry', \
                   author=jane)
    session.add_all([entry1, entry2])
    session.commit()

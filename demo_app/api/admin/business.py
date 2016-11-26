from demo_app import db
from demo_app.blog.models import Author, Category

from flask_restplus import abort

from sqlalchemy.exc import DataError, IntegrityError

def create_category(data):
    try:
        name = data.get('name')
        category = Category(name)
        db.session.add(category)
        db.session.commit()
    except (DataError, IntegrityError):
        db.session.rollback()
        abort(404)

def update_category(id, data):
    try:
        category = Category.query.filter(Category.id==id).one()
        category.name = data.get('name')
        db.session.add(category)
        db.session.commit()
    except (DataError, IntegrityError):
        db.session.rollback()
        abort(404)

def delete_category(id):
    category = Category.query.filter(Category.id==id).one()
    db.session.delete(category)
    db.session.commit()

def create_author(data):
    try:
        name = data.get('name')
        description = data.get('description')
        email = data.get('email')
        author = Author(name, description, email)
        db.session.add(author)
        db.session.commit()
    except (DataError, IntegrityError):
        db.session.rollback()
        abort(404)

def update_author(id, data):
    try:
        author = Author.query.filter(Author.id==id).one()
        author.name = data.get('name')
        author.description = data.get('description')
        author.email = data.get('email')
        db.session.add(author)
        db.session.commit()
    except (DataError, IntegrityError):
        db.session.rollback()
        abort(404)

def delete_author(id):
    author = Author.query.filter(Author.id==id).one()
    db.session.delete(author)
    db.session.commit()

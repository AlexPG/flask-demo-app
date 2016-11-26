from demo_app import db
from demo_app.blog.models import Category

from flask_restplus import abort

from sqlalchemy.exc import IntegrityError

def create_category(data):
    try:
        name = data.get('name')
        category = Category(name)
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(404)

def update_category(id, data):
    try:
        category = Category.query.filter(Category.id==id).one()
        category.name = data.get('name')
        db.session.add(category)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(404)


def delete_category(id):
    category = Category.query.filter(Category.id==id).one()
    db.session.delete(category)
    db.session.commit()

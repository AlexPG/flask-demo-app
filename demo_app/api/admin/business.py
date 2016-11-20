from demo_app import db
from demo_app.blog.models import Category

def create_category(data):
    name = data.get('name')
    category = Category(name)
    db.session.add(category)
    db.session.commit()

def update_category(id, data):
    category = Category.query.filter(Category.id==id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()

def delete_category(id):
    category = Category.query.filter(Category.id==id).one()
    db.session.delete(category)
    db.session.commit()

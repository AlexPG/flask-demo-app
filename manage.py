import os

from flask_script import Manager, Server

from demo_app import create_app, db
from demo_app.blog.models import Author, Category, Entry

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

manager.add_command('runserver', Server())

@manager.command
def createdb():
    """
    Creates a database
    """
    db.create_all()

if __name__ == '__main__':
    manager.run()
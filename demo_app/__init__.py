from flask import Flask

from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
debug_toolbar = DebugToolbarExtension()
migrate = Migrate()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    debug_toolbar.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main as mainModule
    app.register_blueprint(mainModule)

    from .admin import admin as adminModule
    app.register_blueprint(adminModule, url_prefix='/admin')

    from .blog import blog as blogModule
    app.register_blueprint(blogModule, url_prefix='/blog')

    return app

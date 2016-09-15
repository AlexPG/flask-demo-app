from flask import Flask

from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
debug_toolbar = DebugToolbarExtension()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    debug_toolbar.init_app(app)
    db.init_app(app)

    from .main import main as mainModule
    app.register_blueprint(mainModule)

    return app
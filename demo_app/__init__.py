from flask import Flask

from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension

from config import config

bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    debug_toolbar.init_app(app)

    from .blog import blog as blogModule
    app.register_blueprint(blogModule)

    return app
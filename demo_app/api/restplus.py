from flask import current_app as app
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

api = Api(version='1.0', title='Demo App API',
          description='Demo App API')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'

    if not app.config[FLASK_DEBUG]:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    return {'message': 'A database result was required but none was found.'}, 404

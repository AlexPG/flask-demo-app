from flask import Blueprint

from demo_app.api.restplus import api
from demo_app.api.admin.endpoints.categories import ns as admin_categories_namespace
from demo_app.api.admin.endpoints.authors import ns as admin_authors_namespace
from demo_app.api.admin.endpoints.entries import ns as admin_entries_namespace

api_blueprint = Blueprint('api', __name__)
api.init_app(api_blueprint)
api.add_namespace(admin_categories_namespace)
api.add_namespace(admin_authors_namespace)
api.add_namespace(admin_entries_namespace)

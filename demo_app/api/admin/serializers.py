from flask_restplus import fields
from demo_app.api.restplus import api

category = api.model('Category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a category'),
    'name': fields.String(required=True, description='Category name'),
    })

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_categories = api.inherit('Page of categories', pagination, {
    'items': fields.List(fields.Nested(category))
})

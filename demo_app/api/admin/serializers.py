from flask_restplus import fields
from demo_app.api.restplus import api

category = api.model('Category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a category'),
    'name': fields.String(required=True, description='Category name', min_length=1, max_length=50),
    })

author = api.model('Author', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an author'),
    'name': fields.String(required=True, description='Author name', min_length=1, max_length=50),
    'description': fields.String(description='Author description'),
    'email': fields.String(required=True, description='Author email', pattern='[^@]+@[^@]+\.[^@]+', min_length=1, max_length=120),
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

page_of_authors = api.inherit('Page of categories', pagination, {
    'items': fields.List(fields.Nested(author))
})

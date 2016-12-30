from flask_restplus import fields
from demo_app.api.restplus import api

category = api.model('Category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a category'),
    'name': fields.String(required=True, description='Category name', min_length=1, max_length=50)
    })

blog = api.model('Blog main', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an entry'),
    'title': fields.String(required=True, description='Entry title', min_length=1, max_length=50),
    'body': fields.String(required=True, description='Entry body', min_length=1),

    'author_id': fields.Integer(required=True, description='Entry author')
    })

blog_detail = api.inherit('Blog detail', blog, {
    'en_ca': fields.List(fields.Nested(category))
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_blog = api.inherit('Page of blog', pagination, {
    'items': fields.List(fields.Nested(blog))
})

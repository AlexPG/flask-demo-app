from flask import request
from flask_restplus import Resource

from demo_app.api.restplus import api
from demo_app.api.blog.parsers import pagination_arguments
from demo_app.api.blog.serializers import blog, blog_detail, page_of_blog
from demo_app.blog.models import Author, Category, Entry

ns = api.namespace('blog', description='Demo-app blog')

@ns.route('/')
class BlogCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_blog)
    def get(self):
        """
        Returns a list of all blog entries.
        Use this method to get all blog entries.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        entries_query = Entry.query
        entries_page = entries_query.paginate(page, per_page, error_out=False)

        return entries_page

@ns.route('/<int:id>')
@api.response(404, 'Entry not found.')
class BlogItem(Resource):

    @api.marshal_with(blog_detail)
    def get(self, id):
        """
        Returns one blog entry.
        Use this method to get one blog entry.
        * Specify the ID of the entry to get in the request URL path.
        """
        return Entry.query.filter(Entry.id == id).one()

@ns.route('/search/by_author/<string:name>')
class BlogByAuthor(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_blog)
    def get(self, name):
        """
        Returns a list of all blog entries filtered by author.
        Use this method to get one authors entries.
        """
        author = Author.query.filter_by(name=name).subquery()

        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        entries_query = Entry.query.filter(Entry.author_id==author.c.id)
        entries_page = entries_query.paginate(page, per_page, error_out=False)

        return entries_page

@ns.route('/search/by_category/<string:name>')
class BlogByCategory(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_blog)
    def get(self, name):
        """
        Returns a list of all blog entries filtered by category.
        Use this method to get one category entries.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        entries_query = entries = Entry.query.filter(Entry.en_ca.any(name=name))
        entries_page = entries_query.paginate(page, per_page, error_out=False)

        return entries_page

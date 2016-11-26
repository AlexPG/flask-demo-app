from flask import request
from flask_restplus import Resource

from demo_app.api.restplus import api
from demo_app.api.admin.business import create_author, update_author, delete_author
from demo_app.api.admin.parsers import pagination_arguments
from demo_app.api.admin.serializers import author, page_of_authors

from demo_app.blog.models import Author

ns = api.namespace('admin/authors', description='Operations related to admin authors')

@ns.route('/')
class AuthorCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_authors)
    def get(self):
        """
        Returns a list of authors.
        Use this method to get all authors.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        authors_query = Author.query
        authors_page = authors_query.paginate(page, per_page, error_out=False)

        return authors_page

    @api.response(201, 'Author successfully created.')
    @api.expect(author)
    def post(self):
        """
        Creates an author.
        Use this method to create an author.
        * Send a JSON object with the name, description and email in the request body.
        ```
        {
          "name": "Author Name",
          "description": "Author Description",
          "email": "Author Email"
        }
        ```
        """
        data = request.json
        create_author(data)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Author not found.')
class AuthorItem(Resource):

    @api.marshal_with(author)
    def get(self, id):
        """
        Returns one author.
        Use this method to get one author.
        * Specify the ID of the author to get in the request URL path.
        """
        return Author.query.filter(Author.id == id).one()

    @api.response(204, 'Author successfully updated.')
    @api.expect(author)
    def put(self, id):
        """
        Updates an author.
        Use this method to change an author.
        * Send a JSON object with the new name, description and email in the request body.
        ```
        {
          "name": "New Author Name",
          "description": "New Author Description",
          "email": "New Author Email"
        }
        ```
        * Specify the ID of the author to modify in the request URL path.
        """
        data = request.json
        update_author(id, data)
        return None, 204

    @api.response(204, 'Author successfully deleted.')
    def delete(self, id):
        """
        Deletes an author.
        Use this method to delete an author.
        * Specify the ID of the author to delete in the request URL path.
        """
        delete_author(id)
        return None, 204

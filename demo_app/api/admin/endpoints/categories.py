from flask import request
from flask_restplus import Resource

from demo_app.api.restplus import api
from demo_app.api.admin.business import create_category, update_category, delete_category
from demo_app.api.admin.parsers import pagination_arguments
from demo_app.api.admin.serializers import category, page_of_categories

from demo_app.blog.models import Category

ns = api.namespace('admin/categories', description='Operations related to admin categories')

@ns.route('/')
class CategoryCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_categories)
    def get(self):
        """
        Returns a list of categories.
        Use this method to get all categories.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        categories_query = Category.query
        categories_page = categories_query.paginate(page, per_page, error_out=False)

        return categories_page

    @api.response(201, 'Category successfully created.')
    @api.expect(category)
    def post(self):
        """
        Creates a category.
        Use this method to create a category.
        * Send a JSON object with the name in the request body.
        ```
        {
          "name": "Category Name"
        }
        ```
        """
        data = request.json
        create_category(data)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.marshal_with(category)
    def get(self, id):
        """
        Returns one category.
        Use this method to get one category.
        * Specify the ID of the category to get in the request URL path.
        """
        return Category.query.filter(Category.id == id).one()

    @api.response(204, 'Category successfully updated.')
    @api.expect(category)
    def put(self, id):
        """
        Updates a category.
        Use this method to change the name of a category.
        * Send a JSON object with the new name in the request body.
        ```
        {
          "name": "New Category Name"
        }
        ```
        * Specify the ID of the category to modify in the request URL path.
        """
        data = request.json
        update_category(id, data)
        return None, 204

    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        """
        Deletes a category.
        Use this method to delete a category.
        * Specify the ID of the category to delete in the request URL path.
        """
        delete_category(id)
        return None, 204

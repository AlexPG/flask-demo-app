from flask import request
from flask_restplus import Resource

from demo_app.api.restplus import api
from demo_app.api.admin.business import create_entry, update_entry, delete_entry
from demo_app.api.admin.parsers import pagination_arguments
from demo_app.api.admin.serializers import entry, page_of_entries
from demo_app.blog.models import Entry

ns = api.namespace('admin/entries', description='Operations related to admin entries')

@ns.route('/')
class EntryCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_list_with(page_of_entries)
    def get(self):
        """
        Returns a list of entries.
        Use this method to get all entries.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        entries_query = Entry.query
        entries_page = entries_query.paginate(page, per_page, error_out=False)

        return entries_page

    @api.response(201, 'Entry successfully created.')
    @api.expect(entry)
    def post(self):
        """
        Creates an entry.
        Use this method to create an entry.
        * Send a JSON object with the title, body, author and related categories in the request body.
        ```
        {
          "title": "Entry Title",
          "body": "Entry Body",
          "author_id": "Entry Author",
          "en_ca": Entry Category List"
        }
        ```
        """
        data = request.json
        create_entry(data)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'Entry not found.')
class EntryItem(Resource):

    @api.marshal_with(entry)
    def get(self, id):
        """
        Returns one entry.
        Use this method to get one entry.
        * Specify the ID of the entry to get in the request URL path.
        """
        return Entry.query.filter(Entry.id == id).one()

    @api.response(204, 'Entry successfully updated.')
    @api.expect(entry)
    def put(self, id):
        """
        Updates an entry.
        Use this method to change the title, body, author or categories of an entry.
        * Send a JSON object with the new data in the request body.
        ```
        {
          "title": "Entry Title",
          "body": "Entry Body",
          "author_id": "Entry Author",
          "en_ca": Entry Category List"
        }
        ```
        * Specify the ID of the entry to modify in the request URL path.
        """
        data = request.json
        update_entry(id, data)
        return None, 204

    @api.response(204, 'Entry successfully deleted.')
    def delete(self, id):
        """
        Deletes an entry.
        Use this method to delete an entry.
        * Specify the ID of the entry to delete in the request URL path.
        """
        delete_entry(id)
        return None, 204

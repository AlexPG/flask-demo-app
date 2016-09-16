from flask import render_template

from . import admin
from demo_app.blog.models import Author  

@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')

@admin.route('/authors', methods=['GET'])
def authors():
    authors = Author.query.all()
    return render_template('admin/authors/authors_list.html', authors=authors)
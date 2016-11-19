from flask import abort, render_template, current_app as app

from . import blog
from .models import Author, Entry

@blog.route('/', methods=['GET'])
@blog.route('/<int:page>', methods=['GET'])
def index(page=1):
    entries = Entry.query.order_by('title desc').paginate(page, app.config['PER_PAGE'], False)
    return render_template('blog/index.html', entries=entries)

@blog.route('/entry/<int:entry_id>', methods=['GET'])
def entry_detail(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first()
    if entry is not None:
        return render_template('blog/entry_detail.html', entry=entry)
    return abort(404)

@blog.route('/search/by_author/<string:name>', methods=['GET'])
@blog.route('/search/by_author/<string:name>/<int:page>', methods=['GET'])
def search_by_author(name, page=1):
    author = Author.query.filter_by(name=name).subquery()
    entries = Entry.query.filter(Entry.author_id==author.c.id).paginate(page, app.config['PER_PAGE'], False)
    return render_template('blog/by_author.html', entries=entries)

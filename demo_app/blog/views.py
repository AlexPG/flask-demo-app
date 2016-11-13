from flask import abort, render_template, current_app as app

from . import blog
from .models import Entry

@blog.route('/', methods=['GET'])
@blog.route('/<int:page>', methods=['GET'])
def index(page=1):
    entries = Entry.query.order_by('title').paginate(page, app.config['PER_PAGE'], False)
    return render_template('blog/index.html', entries=entries)

@blog.route('/entry/<int:entry_id>', methods=['GET'])
def entry_detail(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first()
    if entry is not None:
        return render_template('blog/entry_detail.html', entry=entry)
    return abort(404)

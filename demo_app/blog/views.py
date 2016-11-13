from flask import render_template, current_app as app

from . import blog
from .models import Entry

@blog.route('/', methods=['GET'])
@blog.route('/<int:page>', methods=['GET'])
def index(page=1):
    entries = Entry.query.order_by('title desc').paginate(page, app.config['PER_PAGE'], False)
    return render_template('blog/index.html', entries=entries)
    
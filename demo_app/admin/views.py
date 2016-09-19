from flask import flash, render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError

from . import admin
from .forms import AuthorForm

from demo_app import db
from demo_app.blog.models import Author  

@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')

@admin.route('/authors', methods=['GET'])
def authors():
    authors = Author.query.all()
    return render_template('admin/authors/authors_list.html', authors=authors)

@admin.route('/authors/create', methods=['GET', 'POST'])
def create_author():
    form = AuthorForm()
    try:
        if form.validate_on_submit():
            author = Author(
                        name = form.name.data,
                        description = form.description.data,
                        email = form.email.data
                    )
            db.session.add(author)
            db.session.commit()
            flash('Author has been successfully created')
            return redirect(url_for('admin.authors'))
    except IntegrityError:
        flash('Email must be unique')
        return render_template('admin/authors/authors_create.html', form=form)
    return render_template('admin/authors/authors_create.html', form=form)

from flask import abort, flash, render_template, redirect, url_for
from sqlalchemy.exc import IntegrityError

from . import admin
from .forms import AuthorForm

from demo_app import db
from demo_app.blog.models import Author  

@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')

# Authors views
@admin.route('/authors', methods=['GET'])
def authors():
    authors = Author.query.all()
    return render_template('admin/authors/author_list.html', authors=authors)

@admin.route('/authors/<int:author_id>', methods=['GET'])
def author_detail(author_id):
    author = Author.query.filter_by(id=author_id).first()
    if author is not None:
        return render_template('admin/authors/author_detail.html', author=author)
    return abort(404)

@admin.route('/authors/create', methods=['GET', 'POST'])
def author_create():
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
        db.session.rollback()
        flash('Email must be unique')
        return render_template('admin/authors/author_create.html', form=form), 404
    return render_template('admin/authors/author_create.html', form=form)

@admin.route('/authors/update/<int:author_id>', methods=['GET', 'POST'])
def author_update(author_id):
    author = Author.query.filter_by(id=author_id).first()
    if author is None:
        return abort(404)
    form = AuthorForm(obj=author)
    try:
        if form.validate_on_submit():
            if form.name:
                author.name = form.name.data
            if form.description:
                author.description = form.description.data
            if form.email:
                author.email = form.email.data
            db.session.commit()
            flash('Author has been successfully updated')
            return redirect(url_for('admin.authors'))
    except IntegrityError:
        db.session.rollback()
        flash('Email must be unique')
        return render_template('admin/authors/author_update.html', form=form, author=author), 404
    return render_template('admin/authors/author_update.html', form=form, author=author)

from flask import abort, flash, render_template, redirect, url_from flask import current_app as appfor
from flask import current_app as app
from sqlalchemy.exc import IntegrityError

from . import admin
from .forms import AuthorForm, CategoryForm, EntryForm

from demo_app import db
from demo_app.blog.models import Author, Category, Entry

@admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.html')

# Author views
@admin.route('/authors', methods=['GET'])
def authors():
    authors = Author.query.order_by('id').all()
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
        flash('Author email must be unique')
        return render_template('admin/authors/author_update.html', form=form, author=author), 404
    return render_template('admin/authors/author_update.html', form=form, author=author)

@admin.route('/authors/delete/<int:author_id>', methods=['GET'])
def author_delete(author_id):
    author = Author.query.filter_by(id=author_id).first()
    if author is None:
        return abort(404)
    db.session.delete(author)
    db.session.commit()
    flash('Author has been successfully deleted')
    return redirect(url_for('admin.authors'))

# Category views
@admin.route('/categories', methods=['GET'])
@admin.route('/categories/<int:page>', methods=['GET'])
def categories(page=1):
    categories = Category.query.order_by('id').paginate(page, app.config['PER_PAGE'], False)
    return render_template('admin/categories/category_list.html', categories=categories)
    
@admin.route('/categories/create', methods=['GET', 'POST'])
def category_create():
    form = CategoryForm()
    try:
        if form.validate_on_submit():
            category = Category(
                        name = form.name.data
                    )
            db.session.add(category)
            db.session.commit()
            flash('Category has been successfully created')
            return redirect(url_for('admin.categories'))
    except IntegrityError:
        db.session.rollback()
        flash('Category name must be unique')
        return render_template('admin/categories/category_create.html', form=form), 404
    return render_template('admin/categories/category_create.html', form=form)

@admin.route('/categories/update/<int:category_id>', methods=['GET', 'POST'])
def category_update(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if category is None:
        return abort(404)
    form = CategoryForm(obj=category)
    try:
        if form.validate_on_submit():
            if form.name:
                category.name = form.name.data
            db.session.commit()
            flash('Category has been successfully updated')
            return redirect(url_for('admin.categories'))
    except IntegrityError:
        db.session.rollback()
        flash('Category name must be unique')
        return render_template('admin/categories/category_update.html', form=form, category=category), 404
    return render_template('admin/categories/category_update.html', form=form, category=category)

@admin.route('/categories/delete/<int:category_id>', methods=['GET'])
def category_delete(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if category is None:
        return abort(404)
    db.session.delete(category)
    db.session.commit()
    flash('Category has been successfully deleted')
    return redirect(url_for('admin.categories'))

# Entry views
@admin.route('/entries', methods=['GET'])
def entries():
    entries = Entry.query.order_by('id').all()
    return render_template('admin/entries/entry_list.html', entries=entries)

@admin.route('/entries/<int:entry_id>', methods=['GET'])
def entry_detail(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first()
    if entry is not None:
        return render_template('admin/entries/entry_detail.html', entry=entry)
    return abort(404)

@admin.route('/entries/create', methods=['GET', 'POST'])
def entry_create():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(
                    title = form.title.data,
                    body = form.body.data,
                    author=form.author.data,
                )
        for c in form.category.data:
            entry.en_ca.append(c)
        db.session.add(entry)
        db.session.commit()
        flash('Entry has been successfully created')
        return redirect(url_for('admin.entries'))
    return render_template('admin/entries/entry_create.html', form=form)

@admin.route('/entries/update/<int:entry_id>', methods=['GET', 'POST'])
def entry_update(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first()
    if entry is None:
        return abort(404)
    form = EntryForm(obj=entry)
    if form.validate_on_submit():
        if form.title:
            entry.title = form.title.data
        if form.body:
            entry.body = form.body.data
        if form.author:
            entry.author = form.author.data
        if form.category.data:
            entry.refresh_categories()
            for c in form.category.data:
                entry.en_ca.append(c)
        db.session.commit()
        flash('Entry has been successfully updated')
        return redirect(url_for('admin.entries'))
    return render_template('admin/entries/entry_update.html', form=form, entry=entry)

@admin.route('/entries/delete/<int:entry_id>', methods=['GET'])
def entry_delete(entry_id):
    entry = Entry.query.filter_by(id=entry_id).first()
    if entry is None:
        return abort(404)
    db.session.delete(entry)
    db.session.commit()
    flash('Entry has been successfully deleted')
    return redirect(url_for('admin.entries'))
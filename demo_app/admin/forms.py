from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Email, InputRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

from demo_app.blog.models import Author, Category

class AuthorForm(Form):
    name = StringField('Name', \
                        validators=[InputRequired( \
                                    message='You must provide an author name')],
                                    description='Authors name')
    description = TextAreaField('Description', \
                                description='A brief information about you')
    email = StringField('Email',
                        validators=[Email( message='Must be email'), \
                                    InputRequired( \
                                    message='You must provide an author email')], \
                                    description='An unique email')

class CategoryForm(Form):
    name = StringField('Name',
                        validators=[InputRequired( \
                                    message='You must provide a category name')], \
                                    description='An unique category name')

def author_list():
    return Author.query.all()

def category_list():
    return Category.query.all()


class EntryForm(Form):
    title = StringField('Title', \
                        validators=[InputRequired( \
                                    message='You must provide a title')],
                                    description='Entry title')
    body = TextAreaField('Body', \
                         validators=[InputRequired( \
                                     message='You must provide some content')],
                                     description='Entry body')
    author = QuerySelectField('Authors', query_factory=author_list, 
                              validators= [InputRequired( \
                                           message='Auhtor cannot be blank')])
    category = QuerySelectMultipleField('Categories', query_factory=category_list, allow_blank=True)

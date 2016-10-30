from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Email, InputRequired, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

from demo_app.blog.models import Author, Category

def name_length_check(form, field):
    if len(field.data) > 50:
        raise ValidationError('Name must be less than 50 characters')

class AuthorForm(Form):
    name = StringField('Name', \
                        validators=[InputRequired( \
                                    message='You must provide an author name'), \
                                    name_length_check],
                                    description='Authors name')
    description = TextAreaField('Description', \
                                description='A brief information about you')
    email = StringField('Email',
                        validators=[Email(message='Must be email'), \
                                    InputRequired( \
                                    message='You must provide an author email')], \
                                    description='An unique email')

    def validate_email(form, field):
        if len(field.data) > 120:
            raise ValidationError('Email must be less than 120 characters')

class CategoryForm(Form):
    name = StringField('Name',
                        validators=[InputRequired( \
                                    message='You must provide a category name'), \
                                    name_length_check], \
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

    def validate_title(form, field):
        if len(field.data) > 50:
            raise ValidationError('Title must be less than 50 characters')

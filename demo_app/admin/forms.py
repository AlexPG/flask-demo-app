from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import Email, InputRequired

class AuthorForm(Form):
    name = StringField('Name', \
                       validators=[InputRequired( \
                                    message='You must provide a name')],
                                    description='Authors name')
    description = TextAreaField('Description', \
                                  description='A brief information about you')
    email = StringField('Email', 
                        validators=[Email( message='Must be email'), \
                                    InputRequired( \
                                     message='You must provide an email')], \
                                     description='An unique email')

class CategoryForm(Form):
    name = StringField('Name', 
                        validators=[InputRequired( \
                                     message='You must provide a name')], \
                                     description='An unique category name')
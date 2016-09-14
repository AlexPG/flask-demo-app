from flask import render_template

from . import blog    

@blog.route('/', methods=['GET'])
def hello():
    return "Hello World from blog module!"
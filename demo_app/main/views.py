from flask import render_template

from . import main    

@main.route('/', methods=['GET'])
def hello():
    return render_template('main/index.html')
from flask import render_template

from . import blog    

@blog.route('/', methods=['GET'])
def hello():
    return render_template('blog/index.html')
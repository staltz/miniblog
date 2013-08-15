
from flask import render_template, request
from miniblog import app
from miniblog.models import Post


@app.route('/')
def index():
    context = {
        'posts': Post.query.all()
    }
    return render_template('index.html', **context)

from flask import render_template
from miniblog import app
from miniblog.posts.models import Post


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

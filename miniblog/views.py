from flask import render_template, request
from miniblog import app
from miniblog.models import Post


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_id>')
def view_post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)

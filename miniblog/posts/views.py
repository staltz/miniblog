from flask import render_template
from miniblog import app
from miniblog.posts.models import Post


@app.route('/posts/<int:post_id>')
def view_post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)


@app.route('/posts/add', methods=['GET', 'POST'])
def add_post():
	# TODO
	return None

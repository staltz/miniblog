from datetime import datetime
from wtforms_alchemy import ModelForm
from miniblog import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.pub_date = datetime.utcnow()

    def __repr__(self):
        return '<Post "%s">' % self.title


class PostForm(ModelForm):
    class Meta:
        model = Post 

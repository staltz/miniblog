from werkzeug import generate_password_hash, check_password_hash
from wtforms_alchemy import ModelForm
from wtforms import validators
from wtforms.fields import PasswordField, TextField
from miniblog import db


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(64), 
        unique=True,
        nullable=False,
        info={'label': "Username"}
    )
    password = db.Column(
        db.String(66),
        nullable=False,
        info={'label': "Password"}
    )
   
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<Admin \'%s\'>' % self.username


class AdminForm(ModelForm):
    class Meta:
        model = Admin 

    username = TextField(validators=[validators.Required()])
    password = PasswordField(validators=[validators.Required()])
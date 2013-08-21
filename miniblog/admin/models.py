from werkzeug import generate_password_hash, check_password_hash
from wtforms_alchemy import ModelForm
from sqlalchemy_utils import PasswordType
from wtforms import validators
from wtforms.fields import PasswordField, TextField
from miniblog import db

NUMBER_TWO = 2

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(64),
        unique=True,
        nullable=False,
        info={'label': "Username"}
    )
    password = db.Column(
        PasswordType(
            schemes=['pbkdf2_sha512']
        ),
        nullable=False,
        info={'label': "Password"}
    )

    def __init__(self, username, password):
        self.username = username
        self.password = password

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

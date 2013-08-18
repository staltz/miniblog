from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy_utils import PasswordType
from wtforms_alchemy import ModelForm
from miniblog import db


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(64), 
        unique=True,
        info={'label': "Username"}
    )
    password = db.Column(
        PasswordType(schemes=['pbkdf2_sha512']),
        nullable=False,
        info={'label': "Password"}
    )

    def __init__(self, password):
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
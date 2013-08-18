import os
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    os.environ.get('HEROKU_POSTGRESQL_ORANGE_URL')
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'should-be-confidential'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from miniblog import views, models
from miniblog.admin import views, models

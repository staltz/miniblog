import os
from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from miniblog.utils import set_db_env_var


app = Flask(__name__)
if os.environ.get('DATABASE_URL') is None:
	set_db_env_var()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'should-be-confidential'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


from miniblog import views, models
from miniblog.admin import views, models

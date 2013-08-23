import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
import sqlalchemy as sa
from sqlalchemy_utils import coercion_listener
from miniblog.utils import set_db_env_var


app = Flask(__name__)
if os.environ.get('DATABASE_URL') is None:
    set_db_env_var()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'should-be-confidential'
db = SQLAlchemy(app)
sa.event.listen(sa.orm.mapper, 'mapper_configured', coercion_listener)
login_manager = LoginManager()
login_manager.init_app(app)


from miniblog import views
from miniblog.posts import views, models
from miniblog.auth import views, models

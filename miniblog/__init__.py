
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    os.environ.get('HEROKU_POSTGRESQL_ORANGE_URL')
db = SQLAlchemy(app)


from miniblog import views, models

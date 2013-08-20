#!venv/bin/python
from miniblog.utils import set_db_env_var
import IPython
from miniblog import app
from miniblog import db


IPython.embed()
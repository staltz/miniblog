#!venv/bin/python
from miniblog import app
from miniblog.utils import set_db_env_var


app.run(debug=True, host='0.0.0.0')

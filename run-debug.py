#!venv/bin/python
from subprocess import Popen, PIPE
import os
from miniblog import app


print " * Importing config vars from Heroku"
postgresql_uri_label = 'HEROKU_POSTGRESQL_ORANGE_URL'
postgresql_uri = Popen(
    'heroku config | grep %s' % postgresql_uri_label,
    stdout=PIPE, shell=True
).stdout.read().splitlines()[0].split()[1]
os.environ[postgresql_uri_label] = postgresql_uri

app.run(debug=True)

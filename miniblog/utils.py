from subprocess import Popen, PIPE
import os


def set_db_env_var():
    postgresql_uri_label = 'DATABASE_URL'
    postgresql_uri = Popen(
        'heroku config | grep %s' % postgresql_uri_label,
        stdout=PIPE, shell=True
    ).stdout.read().splitlines()[0].split()[1]
    os.environ[postgresql_uri_label] = postgresql_uri

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
os.environ['DATABASE_URL'] = 'sqlite://'
from miniblog import db
from miniblog.admin.models import Admin


class TestLogin:
    def setup_method(self, method):
        db.create_all()

    def teardown_class(cls):
        db.drop_all()

    def test_dummy(self):
        a = Admin(username="erdna", password="rasec")
        db.session.add(a)
        db.session.commit()
        result = Admin.query.filter_by(username="erdna").first()
        assert result is not None

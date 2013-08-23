from miniblog import db, app
from miniblog.auth.models import Admin, AdminForm


class TestLogin:
    def setup_class(cls):
        db.create_all()
        # Create a user
        cls.USERNAME = "foobar"
        cls.PASSWORD = "passme"
        a = Admin(username=cls.USERNAME, password=cls.PASSWORD)
        db.session.add(a)
        db.session.commit()

    def teardown_class(cls):
        db.session.remove()
        db.drop_all()

    def test_user_existence(self):
        admin = Admin.query.filter_by(username=self.USERNAME).first()
        assert admin is not None

    def test_basic_login(self):
        response = app.test_client().post('/login', data={
            'username': self.USERNAME,
            'password': self.PASSWORD
        })
        assert response.status == "302 FOUND"

    def test_empty_username_field(self):
        response = app.test_client().post('/login', data={
            'password': self.PASSWORD
        })
        assert response.status == "200 OK"
        assert "has-error" in response.data
        assert "This field is required" in response.data

    def test_wrong_password(self):
        response = app.test_client().post('/login', data={
            'username': self.USERNAME,
            'password': "wrongpassword"
        })
        assert response.status == "200 OK"
        assert "has-error" in response.data
        assert "Wrong password" in response.data

    def test_unexistent_username(self):
        response = app.test_client().post('/login', data={
            'username': "mrnobody",
            'password': "passme"
        })
        assert response.status == "200 OK"
        assert "has-error" in response.data
        assert "No such user exists" in response.data

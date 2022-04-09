import unittest
from unittest.mock import MagicMock, patch
from app import home
import flask as Flask
import flask_login
from flask_login import LoginManager
from models import db, Emails
from flask.testing import FlaskClient
from passlib.hash import sha256_crypt


class user_test(unittest.TestCase):
    def setup(self):
        pass

    def test_app_create(self):
        self.app = app
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()

        db.create_all()
        app = Flask(__name__)
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        assert app
        return app

    def test_email_setup(self):
        email = "test"
        password = "password"
        zipcode = "00000"
        emailtoAdd = Emails(email=email, password=password)
        db.session.add(emailtoAdd)
        db.session.commit()
        assert email in db.session

    def test_password_setup(self):
        email = "email2"
        password = "password2"
        zipcode = "11111"
        password = sha256_crypt.hash(password)
        emailtoAdd = Emails(email=email, password=password)
        db.session.add(emailtoAdd)
        db.session.commit()
        assert password in db.session

    def test_location(self):
        expected = "00000"
        actual = result = Emails.query.filter_by(email="test").first()
        assert expected == actual

    def get_spotify_response(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {["id"]["track_name"]["artists"]}

        with patch("app.requests.get") as mock_requests_get:
            mock_requests_get.return_value = mock_response
            self.assertEqual(home("artists"), "carlyraejepson")


if __name__ == "__main__":
    unittest.main()

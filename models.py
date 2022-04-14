# pylint: disable = no-member, too-few-public-methods
"""
importing flask and usermixin
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Emails(UserMixin, db.Model):
    """
    makes db for user
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    zipcode = db.Column(db.String(20), unique=False, nullable=True) # pylint: disable = missing-final-newline

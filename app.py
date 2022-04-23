# pylint: disable = invalid-envvar-default, no-member, redefined-outer-name
"""import libaries and calling other`
files to use their functions"""
import os
import flask
import flask_login
import requests
import random
from flask import session
from flask_login import LoginManager
from dotenv import find_dotenv, load_dotenv
from passlib.hash import sha256_crypt
from weather import weather_info
from sunset import sun_times
from models import db, Emails
from spotify import get_playlist

load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL0")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def user(user_id):
    """
    used by flask
    """
    return Emails.query.get(int(user_id))


def valid_zip(s):
    return len(s) == 5 and s.isdigit()


@app.route("/home", methods=["GET", "POST"])
def home():  # pylint: disable = missing-function-docstring

    if flask.request.method == "POST":
        session["zipcode"] = flask.request.form["zipcode"]
        result = Emails.query.filter_by(email=session.get("email")).first()
        result.zipcode = session.get("zipcode")
        if valid_zip(result.zipcode):
            db.session.commit()
        else:
            flask.flash("invalid zipcode!", "failure")
    zipcode = session.get("zipcode") or "30301"

    token = session.get("token") or ""
    metric_type = flask.request.form.get("metric_options") or "m"
    weather_details, location_details = weather_info(zipcode, metric_type)
    sunset_times = sun_times(location_details["lat"], location_details["lon"])
    playlist_details = get_playlist(weather_details["weather_code"])

    return flask.render_template(
        "home.html",
        zipcode=zipcode,
        token=token,
        playlist_details=playlist_details,
        weather_details=weather_details,
        location_details=location_details,
        sunset_times=sunset_times,
    )

@app.route("/")
def index():
    """
    new start page
    """

    return flask.render_template("landing.html")


@app.route("/handle_login", methods=["GET", "POST"])
def login():
    """
    login
    """
    if flask.request.method == "POST":
        data = flask.request.form
        email = data["email"]
        password = data["password"]
        if len(Emails.query.filter_by(email=email).all()) != 0:
            user = Emails.query.filter_by(email=email).first()
            if sha256_crypt.verify(password, user.password):
                flask_login.login_user(user)
                session["email"] = user.email
                print(session.get("email"))
                return flask.redirect(flask.url_for("home"))
        flask.flash("Your email or password is incorrect!", "danger")
        return flask.redirect(flask.url_for("login"))
    return flask.render_template("login.html")


@app.route("/handle_signup", methods=["GET", "POST"])
def signup():
    """
    signup
    """
    if flask.request.method == "POST":
        data = flask.request.form
        email = data["email"]
        password = data["password"]
        hashPassword = sha256_crypt.hash(password)  # pylint: disable = invalid-name
        emailtoAdd = Emails(
            email=email, password=hashPassword
        )  # pylint: disable = invalid-name
        if len(Emails.query.filter_by(email=email).all()) != 0:
            flask.flash("Email you have typed already exists", "danger")
            return flask.redirect(flask.url_for("signup"))
        db.session.add(emailtoAdd)
        db.session.commit()
        flask.flash("signup has been successful", "success")
        return flask.redirect(flask.url_for("login"))

    return flask.render_template("login.html")

app.run(
    debug=True,
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8888)),
)

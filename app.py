# pylint: disable = invalid-envvar-default, no-member, redefined-outer-name
"""import libaries and calling other`
files to use their functions"""
import email
import os
import flask
import flask_login
from flask import session
from flask_login import LoginManager, current_user
from models import db, Emails
from dotenv import find_dotenv, load_dotenv
from passlib.hash import sha256_crypt
import requests

load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = f"{os.getenv('URL')}/callback"

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


@app.route("/location", methods=["GET", "POST"])
def location():
    if flask.request.method == "POST":

        # print("POST")
        session["zipcode"] = flask.request.form["zipcode"]
        result = Emails.query.filter_by(email=session.get("email")).first()
        result.zipcode = session.get("zipcode")
        db.session.commit()
        return flask.redirect("/home")

    return flask.render_template("location.html")


@app.route("/home")
def home():
    zipcode = session.get("zipcode") or ""
    if zipcode == "":
        return flask.redirect("/location")

    if session.get("token") == None:
        return flask.redirect("/spotify_login")

    return flask.render_template("home.html", zipcode=zipcode)


@app.route("/")
def index():
    """
    new start page
    """

    return flask.redirect(flask.url_for("login"))


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
        flask.flash("Your email or password is incorrect!")
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
        hashPassword = sha256_crypt.hash(password)
        emailtoAdd = Emails(email=email, password=hashPassword)
        if len(Emails.query.filter_by(email=email).all()) != 0:
            flask.flash("Email you have typed already exists")
            return flask.redirect(flask.url_for("signup"))
        db.session.add(emailtoAdd)
        db.session.commit()
        flask.flash("signup has been successful")
        return flask.redirect(flask.url_for("login"))

    return flask.render_template("signup.html")


@app.route("/spotify_login", methods=["GET"])
def spotify_login():
    params = {
        "client_id": client_id,
        "response_type": "token",
        "redirect_uri": redirect_uri,
        "scope": "playlist-read-private"
    }

    resp = requests.get(
        "https://accounts.spotify.com/authorize",
        params=params,
    )

    return flask.redirect(resp.url)


@app.route("/callback", methods=["GET", "POST"])
def callback():
    if flask.request.method == "GET":
        return flask.render_template("callback.html")
    else:
        session["token"] = flask.request.args["token"]
        return flask.redirect("/home")


app.run(
    debug=True,
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8888)),
)

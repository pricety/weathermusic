# pylint: disable = invalid-envvar-default, no-member, redefined-outer-name
"""import libaries and calling other`
files to use their functions"""
import os
import flask
import flask_login
from flask_login import LoginManager
from models import db, Emails
from dotenv import find_dotenv, load_dotenv
from passlib.hash import sha256_crypt

load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

login_manager = LoginManager()
login_manager.init_app(app)

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

@app.route("/home")
def home():
    return flask.render_template("home.html")

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


app.run(
    debug=True,
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8080)),
)

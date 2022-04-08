# pylint: disable = invalid-envvar-default, no-member, redefined-outer-name
"""import libaries and calling other`
files to use their functions"""
import os
import flask
import flask_login
from flask import session
from flask_login import LoginManager
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

SPOTIFY_GET_TRACK_URL = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'

ACCESS_TOKEN = 'BQD1il3IsV0V1T9TwlRRP8fdSkGmKCiJSusnm7ufvTPDVcpbPNbhB1OGoCMpnnIi6B9H017GKzPMW6DABq3A9lam-aFRsmk3uiibA_9TFvFM_ltzua7CG3Da5eGXbfbCIcohpKoX6JoIjPxuGdkV3wk1dz73zEDScKR24j3dYlwAGcZ1nHUoNrf-echxhwplDCLxkN2uI2m28G0X-4SmRNwSwx60xg'

@login_manager.user_loader
def user(user_id):
    """
    used by flask
    """
    return Emails.query.get(int(user_id))


@app.route("/location", methods=["GET", "POST"])
def location():
    if flask.request.method == "POST":
        print("POST")
        session["zipcode"] = flask.request.form["zipcode"]

        return flask.redirect("/home")

    return flask.render_template("location.html")


@app.route("/home")
def home(access_token):
    zipcode = session.get("zipcode") or ""


    response = requests.get(
        SPOTIFY_GET_TRACK_URL,
        headers={
            "Authorization": "Bearer BQD1il3IsV0V1T9TwlRRP8fdSkGmKCiJSusnm7ufvTPDVcpbPNbhB1OGoCMpnnIi6B9H017GKzPMW6DABq3A9lam-aFRsmk3uiibA_9TFvFM_ltzua7CG3Da5eGXbfbCIcohpKoX6JoIjPxuGdkV3wk1dz73zEDScKR24j3dYlwAGcZ1nHUoNrf-echxhwplDCLxkN2uI2m28G0X-4SmRNwSwx60xg"
        }
    )
    json_resp = response.json()


    track_id = json_resp['album']['id']
    track_name = json_resp['name']
    artists = [artist for artist in json_resp['artists']]

    link = json_resp['external_urls']['spotify']

    artist_names = ', '.join([artist['name'] for artist in artists])

    current_track_info = {
        "id": track_id,
        "track_name": track_name,
        "artists": artist_names,
        "link": link
}

    return flask.render_template(
        "home.html",
        current_track_info=current_track_info,
        zipcode=zipcode
    )


def main():
        current_track_id = None
        while True:
            current_track_info = index(ACCESS_TOKEN)

            if current_track_info['id'] != current_track_id:
                    pprint(
                        current_track_info,
                        indent=4,
                    )
                    current_track_id = current_track_info['id']

            time.sleep(1)














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
    return flask.redirect("/home")


app.run(
    debug=True,
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8888)),
)

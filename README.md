# WEATHERMUSIC

## App Info:

This program recommends a Spotify playlist based on the weather conditions in the area where you are currently located. 

## Install and Run:

If you want to recreate this environment on your device, you will need to install the following requirements:

Flask
python-dotenv
requests
flask_sqlalchemy
sqlalchemy
psycopg2
Postgres
flask_login
passlib

To create a deployment on Heroku, run "heroku create" and "git push heroku main" to your newly created Heroku app. You will also need to create a .env file that includes your Spotify API key and database key (you need to create a Postgres db and link to the Heroku deploy). If you plan on pushing to Github, use a .gitignore file to hide your .env.

# Spotify Accounts Authentication Examples

This project contains basic demos showing the different OAuth 2.0 flows for [authenticating against the Spotify Web API](https://developer.spotify.com/web-api/authorization-guide/).

These examples cover:

* Authorization Code flow
* Client Credentials flow
* Implicit Grant flow

## Installation

These examples run on Node.js. You can find installation instructions on [its website](http://www.nodejs.org/download/). You can also follow [this gist](https://gist.github.com/isaacs/579814) for a quick and easy way to install Node.js and npm.

Once installed, clone the repository and install its dependencies running:

    $ npm install

### Using your credentials
You must register your app and get your credentials from the Spotify for Developers Dashboard.

Go to [your Spotify for Developers Dashboard](https://beta.developer.spotify.com/dashboard) and create your application. For the examples, we registered these Redirect URIs:

* http://localhost:8888 (needed for the implicit grant flow)
* http://localhost:8888/callback

Once you have created your app, replace the `client_id` `redirect_uri` and `client_secret` in the examples with the ones you get from My Applications.

## Running the examples
To run the different examples, open the folder with the name of the flow you want to try out and run its `app.js` file. For instance, to run the Authorization Code example:

    $ cd authorization_code
    $ node app.js

Then, open `http://localhost:8888` in a browser.

## Linting
- missing-function-docstring: functions did not require docstring
- invalid-name: names did not fit the naming convention associated
- no-else-return: block executed return statement for token
- missing-final-newline: adding a new line gave a trailing whitespace error

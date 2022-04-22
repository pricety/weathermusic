# WEATHERMUSIC

This code is currently deployed on heroku here: https://sheltered-wildwood-65723.herokuapp.com/

## App Info:

This program recommends you a Spotify playlist based off of the weather conditions in the area where you are currently located. Development is currently in progress.


## Install and Run:

If you want to recreate this environment on your device, you will need to install the following requirements:

Flask
python-dotenv
requests
flask_sqlalchemy
sqlalchemy
psycopg2
postgres
flask_login
passlib

In order to create a deployment on Heroku, run "heroku create" and "git push heroku main" to your newly created heroku app. You will also need to create a .env file that includes your Spotify API key and database key (you need to create a postgres db and link to the heroku deploy). If you plan on pushing to github, use a .gitignore file to hide your .env.

# Spotify Accounts Authentication Examples

This project contains basic demos showing the different OAuth 2.0 flows for [authenticating against the Spotify Web API](https://developer.spotify.com/web-api/authorization-guide/).

These examples cover:

* Authorization Code flow
* Client Credentials flow
* Implicit Grant flow

## Installation

These examples run on Node.js. On [its website](http://www.nodejs.org/download/) you can find instructions on how to install it. You can also follow [this gist](https://gist.github.com/isaacs/579814) for a quick and easy way to install Node.js and npm.

Once installed, clone the repository and install its dependencies running:

    $ npm install

### Using your own credentials
You will need to register your app and get your own credentials from the Spotify for Developers Dashboard.

To do so, go to [your Spotify for Developers Dashboard](https://beta.developer.spotify.com/dashboard) and create your application. For the examples, we registered these Redirect URIs:

* http://localhost:8888 (needed for the implicit grant flow)
* http://localhost:8888/callback

Once you have created your app, replace the `client_id`, `redirect_uri` and `client_secret` in the examples with the ones you get from My Applications.

## Running the examples
In order to run the different examples, open the folder with the name of the flow you want to try out, and run its `app.js` file. For instance, to run the Authorization Code example do:

    $ cd authorization_code
    $ node app.js

Then, open `http://localhost:8888` in a browser.

## Linting
- missing-function-docstring: functions did not require docstring
- invalid-name: names did not fit the naming convention associated
- no-else-return: block executed return statement for token
- missing-final-newline: adding new line gave trailing whitespace error

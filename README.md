# weathermusic

## App Info:

This program recommends a Spotify playlist based on the weather conditions in the area where you are currently located. Development is currently in progress.

## Install and Run:

If you want to recreate this environment on your device, you will need to install the following requirements:

Flask python-dotenv requests flask_sqlalchemy sqlalchemy psycopg2 postgres flask_login passlib

In order to create a deployment on Heroku, run "heroku create" and "git push heroku main" to your newly created Heroku app. You will also need to create a .env file that includes your Spotify API key and database key (you need to create a Postgres db and link to the Heroku deploy). If you plan on pushing to Github, use a .gitignore file to hide your .env.

# Spotify Accounts Authentication Examples

This project contains basic demos showing the different OAuth 2.0 flows for authenticating against the Spotify Web API.

These examples cover:

Authorization Code flow
Client Credentials flow
Implicit Grant flow
## Installation

These examples run on Node.js. On its website, you can find instructions on how to install it. You can also follow this gist for a quick and easy way to install Node.js and npm.

Once installed, clone the repository and install its dependencies running:

$ npm install
### Using your own credentials

You must register your app and get your credentials from the Spotify for Developers Dashboard.

To do so, go to your Spotify for Developers Dashboard and create your application. For the examples, we registered these Redirect URIs:

http://localhost:8888 (needed for the implicit grant flow)
http://localhost:8888/callback
Once you have created your app, replace the client_id, redirect_uri, and client_secret in the examples with the ones you get from My Applications.

## Running the examples

In order to run the different examples, open the folder with the name of the flow you want to try out and run its app.js file. For instance, to run the Authorization Code example:

$ cd authorization_code
$ node app.js
Then, open http://localhost:8888 in a browser.

## Linting

missing-function-docstring: functions did not require docstring

invalid-name: names did not fit the naming convention associated

no-else-return: block executed return statement for token

missing-final-newline: adding a new line gave a trailing whitespace error

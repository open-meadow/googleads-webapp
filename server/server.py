from flask import Flask, redirect

_CLIENT_URL = "http://localhost:4200"

app = Flask(__name__)

# flow -- will go here first
@app.route("/authorize")
def authorize_endpoint():
    url = "???"
    return redirect(url)

# after generating refresh token, this will redirect back to client URL
@app.route("/oauth2callback")
def oauth2callback_endpoint():
    return redirect(_CLIENT_URL)
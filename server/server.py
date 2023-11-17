from flask import Flask, redirect

app = Flask(__name__)

@app.route("/authorize")
def authorize_endpoint():
    url = "???"
    return redirect(url)
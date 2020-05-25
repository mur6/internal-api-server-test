from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/good")
def good():
    name = "Good"
    return name

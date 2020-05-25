from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return '{"status": "ok"}'


@app.route("/add/<int:integer_number>")
def add(integer_number):
    integer_number += 1
    return str(integer_number)

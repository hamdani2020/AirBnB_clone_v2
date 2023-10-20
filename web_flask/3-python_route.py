#!/usr/bin/python3
"""This script starts a Flask web application
Listening on 0.0.0.0 port 5000.
Routes:
    /: display "Hello HBNB!".
    /hbnb: display "HBNB".
    /c/<text>: display "C", followed by the value of the text
    /python/<text>: display "Python", followed by the value of     the text.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """It displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """It displays hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """It displays c is fun"""
    text = text.replace("_", "")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """It display "Python", followed by the value of the text"""
    text = text.replace("_", "")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

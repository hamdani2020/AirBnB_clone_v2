#!/usr/bin/python3
"""This script starts a flask application.
Listening on 0.0.0.0 port 5000.
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C"
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """It display "Hello HBNB!"."""
    return "Hello HBNB!"

@app.route("/", strict_slashes=False)
def hbnb():
    """It displays "HBNB"."""
    return "HBNB"

app.route("/c/<text>", strict_slashes=False)
def c(text):
    """It displays C followed the value of the text"""
    text = text.replace("_", "")
    return "c {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

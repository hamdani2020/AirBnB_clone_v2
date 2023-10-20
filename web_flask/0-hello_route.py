#!/usr/bin/python3
"""This script runs flask application"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This displays hello world"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

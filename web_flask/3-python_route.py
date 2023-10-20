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


@app.route('/')
def hello():
    """Return string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

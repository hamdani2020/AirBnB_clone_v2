#!/usr/bin/python3
"""This script starts web application with two routings
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """It display a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """It displays a string
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """It displays a string when reformated
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """This function reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """This allows request if the path variable is a valid 
    integer
    """
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

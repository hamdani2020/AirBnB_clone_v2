#!/usr/bin/python3
"""This script starts web application with two routings
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """It displays a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """It displays a string
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """It displays a reformated text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """It displays a reformated string
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """It display an integer
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """It retrieves template for request
    """
    path = '5-number.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

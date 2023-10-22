#!/usr/bin/python3
"""This script starts a flask application"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states")
@app.route("/states/<id>")
def states_list(id=None):
    """This function renders template with states"""
    path = "9-states.html"
    states = storage.all(State)
    return render_template(path, states=states, id=id)


@app.teardown_appcontext
def app_teardown(arg=None):
    """This is a clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

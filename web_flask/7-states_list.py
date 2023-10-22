#!/usr/bin/python3
"""This script starts a flask application
"""

from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    """This renders the template with states
    """
    path = '7-states_list.html'
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """This a clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""This script starts flask application
"""

from models.state import State
from models import storage
from flask import Flask, render_template
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """This funtion renders template with states
    """
    path = '10-hbnb_filters.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(path, states=states, amenities=amenities)


@app.teardown_appcontext
def app_teardown(arg=None):
    """This a clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

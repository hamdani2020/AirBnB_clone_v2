#!/usr/bin/python3
"""This script starts a flask application
"""

from models.state import State
from models import storage
from models.place import Place
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def hbnb_filters():
    """This function renders template with states
    """
    path = '100-hbnb.html'
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template(path, states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def app_teardown(arg=None):
    """This a clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
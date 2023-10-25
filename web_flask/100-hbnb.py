#!/usr/bin/python3
"""A script that starts a Flask web application 12. HBNB is alive!"""

from flask import Flask, render_template, Markup
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def hbnb():
    '''The hbnb home page.'''
    amenities = list(storage.all(Amenity).values())
    all_states = list(storage.all(State).values())
    places = list(storage.all(Place).values())
    amenities.sort(key=lambda x: x.name)
    all_states.sort(key=lambda x: x.name)
    places.sort(key=lambda x: x.name)

    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    pdict = {
        'states': all_states,
        'amenities': amenities,
        'places': places
    }
    return render_template('100-hbnb.html', **pdict)


@app.teardown_appcontext
def flask_teardown(exc):
    '''The Flask app/request for closing storage engine.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

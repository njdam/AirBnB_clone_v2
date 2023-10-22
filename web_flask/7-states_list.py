#!/usr/bin/python3
"""A script to start a Flask web application #8. List of states"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
"""The Flask application strict slashes."""
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Displaying List of States page."""
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda state: state.name)
    pdict = {'states': all_states}
    return (render_template('8-cities_by_states.html', **pdict))


@app.teardown_appcontext
def teardown_flask(exception):
    """After each request you must remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

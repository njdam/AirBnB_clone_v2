#!/usr/bin/python3
"""A script to start a Flask web application #2 HBNB"""

from flask import Flask

# Flask web application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """A flask app to return Hello HBNB!"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """a flsk app to return HBNB"""
    return ("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

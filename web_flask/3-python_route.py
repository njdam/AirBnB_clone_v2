#!/usr/bin/python3
"""A script to start a Flask web application 2. C is fun!"""

from flask import Flask


app = Flask(__name__)
"""The Flask application option"""
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """The home page"""
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """The hbnb page"""
    return ("HBNB")


@app.route('/c/<text>')
def c_page(text):
    """The c page"""
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    """The Python page"""
    return ("Python {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

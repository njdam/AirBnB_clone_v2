#!/usr/bin/python3
"""A script to start a Flask web application 2. C is fun!"""

from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def page_number(n):
    """The number's page"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    """The Number Template page."""
    pdict = {'n': n}
    return (render_template('5-number.html', **pdict))


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Is even or odd number page"""
    if n % 2 == 0:
        pdict = {'n': n, 't': "even"}
    else:
        pdict = {'n': n, 't': "odd"}
    return (render_template('6-number_odd_or_even.html', **pdict))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

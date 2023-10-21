#!/usr/bin/python3
"""A script to start a Flask web application."""

from flask import Flask


app = Flask(__name__)
# app.url_map.strict_slashes = False
# Defining route with strict_slashes=False option


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

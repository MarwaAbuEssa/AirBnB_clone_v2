#!/usr/bin/python3
"""Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /:  'Hello HBNB!'.
    /hbnb:  'HBNB'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
""" Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /:  'Hello HBNB!'.
    /hbnb:  'HBNB'.
    /c/<text>:  'C' then value of <text>.
    /python/(<text>):  'Python' then value of <text>.
    /number/<n>:  'n is a number' only if <n> is int.
    /number_template/<n>:  an HTML page if n is int .
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' then value <text>

    replac _ in <text> /.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' then value <text>

    replac _ in <text> /.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' is int."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """HTML page only if <n> int."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

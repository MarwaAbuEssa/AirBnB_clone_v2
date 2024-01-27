#!/usr/bin/python3
""" Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML all State objects.
    /states/<id>: HTML page state by <id>.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ HTML page a list of States.

    sort by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """HTML page info about <id>"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove SQLAlchemy """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

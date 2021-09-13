#!/usr/bin/python3
"""
This module start the flask web app.
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_flask():
    """
    Print 'Hello HBNB!'
    """
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    """
    Display “HBNB”
    """
    return ("HBNB")


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Display “C ” followed by the value of the text variable.
    """
    return ("C " + text.replace("_", " "))


@app.route("/python")
@app.route('/python/<text>/')
def python_is_cool(text='is cool'):
    """
    Display “Python is cool”
    """
    return 'Python %s' % text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host="0.0.0.0")

#!/usr/bin/python3
""" Module that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """ Returns a string at the root route """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Returns a string at the /hbnb route """
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """ Returns a string at the route, expands the text variable """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python(text):
    """ Returns a string at the route, expands the text variable """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

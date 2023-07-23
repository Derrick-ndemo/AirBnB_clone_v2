#!/usr/bin/python3
"""Module that starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Method that returns a message when
    the route / is taken"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Method returns a message when
    the route /hbnb is taken"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Method returns a message when
    the route /c/<text> is taken"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Method returns a message when
    the route /python/<text> is taken"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """ Method returns a message when
    the route /number/<n> is taken"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_n(n):
    """ Method returns a message when
    the route /number_template/<n> is taken"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_n(n):
    """ Method returns a message when
    the route /number_odd_or_even/<n> is taken"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

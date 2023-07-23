#!/usr/bin/python3
"""Module that finds a path to a number"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Returns hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Returns C followed by text"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Returns Python followed by text"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_n(n):
    """Returns n is a number if n is an integer"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

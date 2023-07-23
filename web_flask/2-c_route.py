#!/usr/bin/python3
""" Flask app """

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """ Hello method """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ HBNB method """
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """ C method """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

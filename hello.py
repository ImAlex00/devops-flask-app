import json
import time

import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host='redis-server', port=6379, decode_responses=True)


def cached(key, build):
    data = r.get(key)
    if data is not None:
        data = json.loads(data)
        if time.time() - data['time'] <= 600:
            return data['html']
    html = build()
    r.set(key, json.dumps({'html': html, 'time': time.time()}))
    return html


@app.route('/')
def say_hello():
    return cached('home', lambda: '<p>Hello, World, I am a Flask app!</p> <br> <p><a href="/about">About</a></p> <p><a href="/contact">Contact</a></p>')


@app.route('/about')
def display_about():
    return cached('about', lambda: '<p>This runs on the <a href="https://flask.palletsprojects.com/en/stable/">Flask</a> framework</p> <p> This was coded on <a href="https://python.org/">Python</a> </p> <p><a href="/">Return</a></p>')


@app.route('/contact')
def display_contact():
    return cached('contact', lambda: '<p>Contact me at: alexhoran2002@gmail.com</p> <p><a href="/">Return</a></p>')

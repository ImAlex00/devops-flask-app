from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
        return '<p>Hello, World, I am a Flask app!</p> <br> <p><a href="/about">About</a></p> <p><a href="/contact">Contact</a></p>'

@app.route('/about')
def display_about():
        return '<p>This runs on the <a href="https://flask.palletsprojects.com/en/stable/">Flask</a> framework</p> <p><a href="/">Return</a></p>'

@app.route('/contact')
def display_contact():
        return '<p>Contact me at: alexhoran2002@gmail.com</p> <p><a href="/">Return</a></p>'

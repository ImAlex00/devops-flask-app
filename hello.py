from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '<p>Hello, World, I am a Flask app!</p> <br> <p><a href="/about"About</a><p>'

@app.route('/about')
def display_about():
	return '<p> This runs on the <a href="https://flask.palletsprojects.com/en/stable/">flask</a> framework</p> <p><a href="/">return</a></p?'

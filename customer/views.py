from flask import render_template
from .__init__ import app

@app.route('/')
def index():
    return 'hello'

@app.route('/login')
def login():
    return render_template('login.html')
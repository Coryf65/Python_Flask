# This file creates the flask app
from flask import Flask, render_template

app = Flask(__name__)

# creating a route
@app.route('/')

def home():    
    # we are going to user our new template
    return render_template('home.html', name='Cory')

# adding another route
@app.route('/about')

# function names and routes don't HAVE to match
def about():
    return 'This is a URL shortener'


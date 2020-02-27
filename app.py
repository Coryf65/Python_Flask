# This file creates the flask app
from flask import Flask, render_template, request

app = Flask(__name__)

# creating a route
@app.route('/')

def home():    
    # we are going to user our new template
    return render_template('home.html')

# adding another route
@app.route('/your-url')

# function names and routes don't HAVE to match
def your_url():
    return render_template('your_url.html', code=request.args['code'])


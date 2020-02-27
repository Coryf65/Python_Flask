# This file creates the flask app
from flask import Flask

app = Flask(__name__)

# this will display 'hello' the name of this file
#print(__name__)

# creating a route
@app.route('/')


def home():
    return 'Hello Flask!'
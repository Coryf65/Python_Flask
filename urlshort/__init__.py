from flask import Flask

# This file creates the flask app

def create_app(test_config=None):
    app = Flask(__name__)
    # if in production you want to generate a very long random key
    app.secret_key = 'hjas83jasnuka9n338793jsa83747239ejekjnwuq938h'

    from . import urlshort

    app.register_blueprint(urlshort.bp)

    return app
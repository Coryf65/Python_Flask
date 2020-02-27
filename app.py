# This file creates the flask app
from flask import Flask, render_template, request, redirect, url_for
import json
import os.path

app = Flask(__name__)

# creating a route
@app.route('/')
def home():    
    # we are going to user our new template
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():

    if request.method == 'POST':
        # creating a Dictionary to store info
        urls = {}

        # checking if we already have this in our file
        if os.path.exists('urls.json'):
            # then we want to open it
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        if request.form['code'] in urls.keys():
            redirect(url_for('home'))

        # specifying the KEY/Name = code, and Value pair
        urls[request.form['code']] = {'url':request.form['url']}

        # saving to JSON file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:        
        return redirect(url_for('home'))


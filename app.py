# This file creates the flask app
from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
# tool to chekc if a file is safe to upload
from werkzeug.utils import secure_filename

app = Flask(__name__)
# if in production you want to generate a very long random key
app.secret_key = 'hjas83jasnuka9n338793jsa83747239ejekjnwuq938h'

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
            # displaying a message
            flash('That shortname has already been taken, Please select another')
            return redirect(url_for('home'))

        # now we check if it is a file or url
        if 'url' in request.form.keys():
            # a url
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            # a file
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('C:/Users/Cory/Documents/_Code/Python_Flask/' + full_name)
            # now update our json file
            urls[request.form['code']] = {'file':full_name}
            
        # saving to JSON file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', code=request.form['code'])
    else:        
        return redirect(url_for('home'))


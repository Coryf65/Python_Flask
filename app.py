# This file creates the flask app
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# creating a route
@app.route('/')
def home():    
    # we are going to user our new template
    return render_template('home.html')

# by default flask uses GET requests
# now we are telling flask to use a POST
@app.route('/your-url', methods=['GET', 'POST'])

# function names and routes don't HAVE to match
def your_url():

    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:        
        return redirect(url_for('home'))


from flask import render_template, request, redirect, url_for, flash, abort, session, jsonify, Blueprint
import json
import os.path
# tool to check if a file is safe to upload
from werkzeug.utils import secure_filename

bp = Blueprint('urlshort', __name__)

# creating a route
@bp.route('/')
def home():    
    # we are going to user our new template
    return render_template('home.html', codes=session.keys())

@bp.route('/your-url', methods=['GET', 'POST'])
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
            f.save('C:/Users/Cory/Documents/_Code/Python_Flask/static/user_files/' + full_name)
            # now update our json file
            urls[request.form['code']] = {'file':full_name}

        # saving to JSON file
        with open('urls.json', 'w') as url_file:
            json.dump(urls, url_file)
            # also want to store as a cookie
            session[request.form['code']] = True
        return render_template('your_url.html', code=request.form['code'])
    else:        
        return redirect(url_for('home'))

# look for any string in the url 
@bp.route('/<string:code>')

def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else: 
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))

    return abort(404)


@bp.errorhandler(404)

def page_not_found(error):
    return render_template('page_not_found.html'), 404

# creating an API based off the codes
@bp.route('/api')

def session_api():
    return jsonify(list(session.keys()))
    
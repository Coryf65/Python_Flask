# Python_Flask
Learning Flask (Flask is a Python framework for building lightweight and dynamic web applications)

Use `/` for paths

## Pros and Cons of Flask

* Pros

  - Easy to get started
  - very customizable
  - Web Server Gateway Interface (WSGI) compatible

* Cons

  - Extremely limited
  - No database help
  
 ## Setup
 
 use pip to install Flask module
 ```bash
 $ pip install flask
 ```
 
 ### Running your WebServer (use Bash terminal)
 
 Point Flask to app Start
 ```bash
$ export FLASK_APP=hello
 ```
 
 running Flask
```bash
$ flask run
 ```

Open a web Browser enter
`http://127.0.0.1:5000/`

![tada!](/_images/first_flask_site.PNG)

Setup for the Dev enviroment to auto update! by telling Flask we are developing it yet.
```bash
$ export FLASK_ENV=development
 ```
 
 you can see our enviroment set = development upon running Flask
![tada!](/_images/flask_dev_env.PNG)

Now we can code and refresh our browser to see our changes!


### Using pytest

this will allow testing our application easier
 ```bash
 $ pip install pytest
 ```

### Deploying

1. install pip on the server

2. export FLASK_APP=urlshort

3. flask run

4. testing to see flask run --host=0.0.0

so instead of using flask we will be using 'gunicorn' "Green Unicorn"
 ```bash
 $ pip install gunicorn
 ```
Then onces it's installed run Gunicorn
 ```bash
 $ gunicorn "urlshort:create_app()" -b 0.0.0.0
 ```
now might run on port 8000

Cntrl+c

We want to use Nginx, if we do not have it already
 ```bash
 $ sudo apt install nginx
 ```

Checking if nginx is running 
 ```bash
 $ systemctl status nginx
 ```
to quit
 ```bash
 $ :q
 ```
 
if we get a Bad Gateway we would need to edit the config file for nginx

### For More info on deployment 

[Gunicorn](https://gunicorn.org/#deployment)


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

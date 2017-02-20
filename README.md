# RESTful-API
RESTful-API developed primarily with Python and Flask
##Installation
```
pip install Flask
pip install Flask-RESTful
pip install Flask-JWT
```

## Description
This API makes use of Python and the web development framework, Flask. 
Ideally, this API would allow a user to sign in and edit their to-do list.  

## Implementation
The API has app.py which is the Flask application. 
The user.py file give the functionality of signing in and registering new users. 
The users each have a username and password that is used for authentication within the security.py file.
The items on the to-do list are created with the task.py file. 
All of the data is stored using SQLite and table.py which creates the .db file for that data.




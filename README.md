flask-template
==============

A base template for a flask project with forms, login etc.
Best to be used for development under virtualenv

Requires
--------

Install requirements using ```pip install -r requirements.txt```.

This installs the following:

- Flask
- Flask-WTF
- Flask-Login
- Flask-SQLAlchemy (for SQL Databases)
- SQLAlchemy-Migrate (for SQL Databases)
- Flask-MongoAlchemy (for MongoDB)

Scripts
-------

The Scripts ```db_create.py```, ```db_migrate.py``` and ```db_upgrade.py``` are meant to be used with SQLAlchemy for migrations

Models
------

An example User model is provided in app/models.py. For SQL database like SQLite you will have to add the following table:

    CREATE TABLE user (
        id INTEGER NOT NULL,
        username VARCHAR(20),
        password VARCHAR(64),
        email VARCHAR(64),
        role SMALLINT, about_me VARCHAR(200), 
        first_name VARCHAR(30), 
        last_name VARCHAR(30), 
        about_me VARCHAR(200),
        created_at DATETIME,
        updated_at DATETIME,
        PRIMARY KEY (id)
    )


TODO
----

- Updated Migrate scripts for the MongoDB models
- etc. - It's open source project, so contributions are welcome



Thanks
------

This template is inspired by [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
and all other cool modules and flask-based projects.


License
-------

The MIT License (MIT)

Copyright (c) [2013] [Vladimir Kolev]

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

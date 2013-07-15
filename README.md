flask-template
==============

A base template for a flask project with forms, login etc.
Best to be used for development under virtualenv

Requires
--------

Flask
Flask-WTF
Flask-Login
Flask-SQLAlchemy (if used with SQL Databases)
SQLAlchemy-Migrate (if used with SQL Databases)
Flask-MongoAlchemy (if used with MongoDB)

Scripts
-------

The Scripts db_create.py, db_migrate.py and db_upgrade.py are meant to be used with SQLAlchemy for migrations

Models
------

An example User model is provided in app/models.py for a SQL database like SQLite you will to add the following table:

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

# Update Migrate scripts for the MongoDB models
# Add requirements for pip installation
# etc. - It's open source project, so contributions are welcome

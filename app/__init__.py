from flask import Flask
# SQLAlchemy import
#from flask.ext.sqlalchemy import SQLAlchemy
# MongoAlcemy import 
from flask.ext.mongoalchemy import MongoAlchemy
# LoginManager is needed for the login process
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
# Setup SQLAlchemy for the project
#db = SQLAlchemy(app)
# Setup MongoAlchemy
db = MongoAlchemy(app)

lm = LoginManager()
lm.session_protection = "strong"
lm.setup_app(app)

from app import views, models

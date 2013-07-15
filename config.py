import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration for SQLite
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Configuration MongoAlchemy
MONGOALCHEMY_DATABASE = "flasktest"

# Used for WTForms
CSRF_ENABLED = True
SECRET_KEY = "justAs1mPl3K3yzT0t357"

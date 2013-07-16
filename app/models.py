from app import db
# When with SQLAlchemy
# from datetime import datetime
import hashlib

ROLE_USER = 0
ROLE_ADMIN = 1

# Model when used with SQLAlchemy

# class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(20), index=True, unique=True)
    # password = db.Column(db.String(64), index=True)
    # email = db.Column(db.String(64), index=True, unique=True)
    # role = db.Column(db.SmallInteger, default=ROLE_USER)
    # first_name = db.Column(db.String(30))
    # last_name = db.Column(db.String(30))
    # about_me = db.Column(db.String(200))
    # created_at = db.Column(db.DateTime(), default=datetime.now())
    # updated_at = db.Column(db.DateTime())

    # def is_authenticated(self):
        # return True

    # def is_active(selt):
        # return True

    # def is_anonymous(self):
        # return False

    # def get_auth_token(self):
        # return unicode(hashlib.sha1(self.username +
        # self.password).hexdigest())

    # def get_id(self):
        # return unicode(self.id)

    # def __repr__(self):
        # return '<User %r>' % (self.username)


class User(db.Document):

    config_collection_name = 'users'

    username = db.StringField()
    password = db.StringField()
    email = db.StringField()
    role = db.IntField(default=ROLE_USER)
    firstname = db.StringField()
    lastname = db.StringField()
    about_me = db.StringField()
    created_at = db.CreatedField()
    updated_at = db.ModifiedField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_auth_token(self):
        return unicode(hashlib.sha1(self.username + self.password).hexdigest())

    def get_id(self):
        return unicode(self.mongo_id)

    def __repr__(self):
        return '<User %r>' % (self.username)

from google.appengine.ext import db

class User(db.Model):
    username = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

class Post(db.Model):
    title = db.StringProperty(required = True)
    body = db.TextProperty(required = True)
    author = db.ReferenceProperty(required = True)
    created = db.DateTimeProperty(User, auto_now_add = True)
    # TODO - we need an author field here; it should be required

# -*- coding: utf-8 -*-
"""
    app.models
    ~~~~~~~~~~~

    Models

    :author: Adam Zucker
"""
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.Integer, index=True)
    name = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(256), index = True)

    def __init__(self, name=None, email=None, role=ROLE_USER, password="password"):
        self.name = name
        self.email = email
        self.role = role
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    title = db.Column(db.String(140))
    picture = db.Column(db.String(256))
    content_type = db.Column(db.String(140))
    link = db.Column(db.String(2086))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime)


    def __init__(self, user_id, link=None, body=None, title=None, picture=None, content_type='UNKNOWN'):
        self.user_id = user_id
        self.body = body
        self.title = title
        self.date_created = datetime.datetime.utcnow()
        self.link = link
        self.picture = picture
        self.content_type = content_type

    def __repr__(self):
        return '<Post %r>' % (self.title)



#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class User"""


from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
db = SQLAlchemy(app)


class User(db.Model):
    """This class represent a user"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Book(db.Model):
    """This class rerpesent a book instance"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

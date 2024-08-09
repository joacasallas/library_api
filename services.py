#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides the methods for user and book classes"""


from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from marshmallow import Schema, fields
from models import db, User, Book


class UserDTO(Schema):
    """validate User values"""
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)


class BookDTO(Schema):
    """Validate Book values"""
    id = fields.Int(dump_only=True)
    title = fields.Str(requred=True)
    author = fields.Str(required=True)


def register_user(username, password):
    """New user - register and password hash"""
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()


def authenticate_user(username, password):
    """New user - authentication"""
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        return create_access_token(identity=username)
    return None


def add_book(title, author):
    """create a new instance of book"""
    new_book = Book(title=title, author=author)
    db.session.add(new_book)
    db.session.commit()


def get_all_books():
    """get all the book instances stored in the DB"""
    return Book.query.all()


def get_book_by_id(book_id):
    """get book but ID"""
    return Book.query.get(book_id)


def update_book(book_id, title, author):
    """update book"""
    book = Book.query.get(book_id)
    if book:
        book.title = title
        book.author = author
        db.session.commit()


def delete_book(book_id):
    """delete book"""
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()

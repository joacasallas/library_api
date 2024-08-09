#!/usr/bin/python3
# Author: Joana Casallas
"""This module define Routes"""


from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from services import register_user, authenticate_user
from services import add_book, get_all_books, get_book_by_id, update_book, delete_book
from services import BookDTO


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/register', methods=['POST'])
def register():
    """register user"""
    data = request.get_json()
    username = data['username']
    password = data['password']
    register_user(username, password)
    return jsonify({"msg": "User registered succesfully"}), 201


@user_routes.route('/login', methods=['POST'])
def login():
    """login user"""
    data = request.get_json()
    username = data['username']
    password = data['password']
    access_token = authenticate_user(username, password)
    if access_token:
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid password"}), 401


@user_routes.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    """get profile user"""
    current_user = get_jwt_identity()
    return jsonify(username=current_user), 200


book_routes = Blueprint('book_routes', __name__)


@book_routes.route('/books', methods=['POST'])
@jwt_required()
def create_book():
    "create a new book instance"
    data = request.get_json()
    try:
        BookDTO().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    add_book(data['title'], data['author'])
    return jsonify({"msg": "Book added"}), 201


@book_routes.route('/books', methods=['GET'])
@jwt_required()
def list_books():
    """get a list of all the books stored"""
    books = get_all_books()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books]), 200


@book_routes.route('/books/<int:book_id>', methods=['GET'])
@jwt_required()
def get_book(book_id):
    """get the book_id information"""
    book = get_book_by_id(book_id)
    if book:
        return jsonify({'id': book.id, 'title': book.title, 'author': book.author}), 200
    return jsonify({"msg": "Book not found"}), 404


@book_routes.route('/books/<int:book_id>', methods=['PUT'])
@jwt_required()
def update(book_id):
    """update book atributtes"""
    data = request.get_json()
    try:
        BookDTO().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    update_book(book_id, data['title'], data['author'])
    return jsonify({"msg": "Book updated"}), 200


@book_routes.route('/books/<int:book_id>', methods=['DELETE'])
@jwt_required()
def delete(book_id):
    """delete book_id"""
    delete_book(book_id)
    return jsonify({"msg": "Book deleted"}), 200

#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Config"""


class Config:
    """configuration"""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'joacasallas'

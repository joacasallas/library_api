#!/usr/bin/python3
# Author: Joana Casallas
"""This module provides a class Config"""

import os


class Config:
    """configuration"""
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "library.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'joacasallas'

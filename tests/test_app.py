"""Tests App"""

import unittest
from flask_jwt_extended import create_access_token
from app import app, db


class FlaskTestCase(unittest.TestCase):
    """tests app"""


    @classmethod
    def setUpClass(cls):
        """setup for each test"""
        app.config['TESTING'] = True
        cls.client = app.test_client()

    def setUp(self):
        """setup for each test"""
        db.create(all)

    def tearDown(self):
        """tearDown for each test"""
        db.drop_all()

    def test_register_user(self):
        """Test the register_user method"""
        response = self.client.post('/register', json={'username': 'Joa', 'password': 'Joa123'})
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        """Test the login_user method"""
        self.client.post('/register', json={'username': 'Joa', 'password': 'Joa123'})
        response = self.client.post('/login', json={'username': 'Joa', 'password': 'Joa123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)

    def test_add_book(self):
        """Test the add_book method"""
        access_token = create_access_token(identity='Joa')
        response = self.client.post('/books', json={'title': 'name_book_123', 'author': 'name_author_123'}, headers={'Authorization': f'Bearer {access_token}'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main-__':
    unittest.main()

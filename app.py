#!/usr/bin/python3
# Author: Joana Casallas
"""App Initialization"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from routes import user_routes, book_routes


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(user_routes)
app.register_blueprint(book_routes)


if __name__ == '__main__':
    app.run(debug=True)

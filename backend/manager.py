from flask import Flask
from flask.blueprints import Blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(blueprints:Blueprint, database: SQLAlchemy):
    app = Flask(__name__)
    database.init_app(app)
    for x in blueprints:
        app.register_blueprint(x)
    database.drop_all()
    database.create_all()
    return app
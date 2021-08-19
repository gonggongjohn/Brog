from flask import Flask
from flask.blueprints import Blueprint
from models import *
from ext import *
import settings
from typing import List

def create_app(blueprints: List[Blueprint], recreate_tables=False) -> Flask:
    app = Flask(__name__)
    app.config.from_object(settings)
    db.init_app(app)
    cors.init_app(app)
    for x in blueprints:
        app.register_blueprint(x)
    if recreate_tables:
        with app.app_context():
            db.drop_all()
            db.create_all()
    return app
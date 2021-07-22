from functools import wraps
from flask import session, request
from flask.helpers import url_for
from models import *
from ..ext import db
import json

def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if db.session.query(User).filter_by(
            id=session.get('id'),
            pwd=session.get('pwd')
        ).first():
            return func(*args, **kwargs)
        else:
            return json.dumps({'status': 404})
    return inner
from functools import wraps
from flask import session, request
from flask.helpers import url_for
from models import *
from ext import db
import json

def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        if ip == session.get('ip'):
            return func(*args, **kwargs)
        if db.session.query(User).filter_by(
            id=session.get('user_id'),
            token=session.get('token')
        ).first():
            return func(*args, **kwargs)
        else:
            return json.dumps({'status': 404, 'reason': 'unauthorized user',}), 404
    return inner
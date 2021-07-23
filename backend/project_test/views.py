import json
from flask.blueprints import Blueprint
from flask import session, request
from models import User
from ext import db

bp = Blueprint(
    name='test',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/test'
)

@bp.route('/see/session/')
def see_session():
    return json.dumps([(x, session[x]) for x in session]), 200

@bp.route('/add/session/')
def add_session():
    session['user'] = 111
    session.modified = True
    session['ip'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return 'ok', 200

@bp.route('/add/user/<name>/<pwd>/')
def add_user(name, pwd):
    db.session.add(User(name=name, pwd=pwd, ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)))
    db.session.commit()
    return 'New User: (username: %s, password: %s, @: %s)'%(name, pwd, request.environ.get('HTTP_X_REAL_IP', request.remote_addr)), 200
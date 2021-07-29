import json
from flask.blueprints import Blueprint
from flask import session, request
from flask.helpers import send_file
from models import User
from ext import db
import os

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
    db.session.add(User(name=name, pwd=pwd, ip=request.environ.get(
        'HTTP_X_REAL_IP', request.remote_addr)))
    db.session.commit()
    return 'New User: (username: %s, password: %s, @: %s)' % (name, pwd, request.environ.get('HTTP_X_REAL_IP', request.remote_addr)), 200


@bp.route('/see/user/')
def see_user():
    return "".join(['<p>(%s, %s, %s)</p>' % (x.name, x.pwd, x.token) for x in db.session.query(User).all()])


@bp.route("/demo_img/", methods=["GET"])
def demo_img():
    pic_name = request.values.get("pic_name")
    return send_file(
        path_or_file=os.path.join(os.path.dirname(__file__), "img", pic_name+".png"),
        as_attachment=True,
        mimetype="text/application"
    )

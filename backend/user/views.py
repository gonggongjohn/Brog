import logging
from flask.blueprints import Blueprint
from flask\
    import request, session, make_response
import json
from models import *
from sqlalchemy import and_, or_
from random import choices

bp = Blueprint(
    name='user',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/user'
)


@bp.route('/login/', methods=["POST", "OPTIONS"])
def login():
    try:
        data = json.loads(request.get_data(as_text=True))
    except:
        return json.dumps({'status': 404, })
    user_obj_qset = db.session.query(User).filter_by(
        name=data["username"],
        pwd=data["password"]
    )
    user_obj = user_obj_qset.first()
    if not user_obj:
        return json.dumps({'status': 404, })
    user_obj_qset.update({
        User.ip: request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    }, synchronize_session='evaluate')
    db.session.commit()
    session.update({
        'user_id': user_obj.id,
        'token': user_obj.token,
        'ip': user_obj.ip,
    })
    session.modified = True
    return json.dumps({'status': 200, })


@bp.route('/register/', methods=["POST", "OPTIONS"])
def register():
    try:
        data = json.loads(request.get_data(as_text=True))
    except:
        return json.dumps({'status': 404, })
    user_obj = User(
        name=data['username'],
        pwd=data['password'],
        ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr),
        id=''.join(choices(string.ascii_letters + string.digits, k=50))
    )
    if db.session.query(User).filter_by(name=user_obj.name).first():
        return json.dumps({'status': 404, }), 200
    while True:
        try:
            db.session.add(user_obj)
            db.session.commit()
            break
        except:
            db.session.rollback()
            user_obj.id = ''.join(
                choices(string.ascii_letters + string.digits, k=50))
    session.update({
        'user_id': user_obj.id,
        'token': user_obj.token,
        'ip': user_obj.ip,
    })
    session.modified = True
    return json.dumps({'status': 200, }), 200

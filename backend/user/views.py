from flask.blueprints import Blueprint
from flask\
    import request, session
import json
from models import *
from sqlalchemy import and_, or_

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
    user_obj_qset.update(
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    )
    db.session.commit()
    session.update({
        'user_id': user_obj.id,
        'token': user_obj.token,
        'ip':user_obj.ip
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
        ip=request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    )
    try:
        db.session.add(user_obj)
        session.update({
            'user_id': user_obj.id,
            'token': user_obj.token,
            'ip':user_obj.ip,
        })
        session.modified = True
        db.session.commit()
        return json.dumps({'status': 200, })
    except:
        db.session.rollback()
        return json.dumps({'status': 404, })
from flask.blueprints import Blueprint
from flask\
    import request, session
import json
from models import *
from sqlalchemy import and_, or_
from ext import cors

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
        print(data) # 调试
    except:
        return json.dumps({'status': 0, })
    user_obj = User.query.filter_by(
        name=data["username"],
        pwd=data["password"]
    ).first()
    if not user_obj:
        return json.dumps({'status': 0, })
    session.update({
        'user_id': user_obj.id,
        'token': user_obj.token
    })
    session.modified = True
    return json.dumps({'status': 1, })


@bp.route('/register/', methods=["POST", "OPTIONS"])
def register():
    print('register')
    try:
        data = json.loads(request.get_data(as_text=True))
        print(data)
    except:
        return json.dumps({'status': 404, })
    user_obj = User(name=data["username"], pwd=data["password"])
    try:
        db.session.add(user_obj)
        return json.dumps({'status': 200, })
    except:
        return json.dumps({'status': 404, })
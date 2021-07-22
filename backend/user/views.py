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


@bp.route('/login/', methods=["POST"])
def login():
    try:
        data = json.loads(request.get_data(as_text=True))
        print(data) # 调试
    except:
        return json.dumps({'status': 404, })
    user_obj = User.query.filter_by(
        name=data["username"],
        pwd=data["password"]
    ).first()
    if not user_obj:
        return json.dumps({'status': 200, })
    session.update({
        'user_id': user_obj.id,
        'token': user_obj.token
    })
    session.modified = True
    return json.dumps({'status': 200, })


@bp.route('/register/', methods=["POST"])
def register():
    return json.dumps({'status': 200, })

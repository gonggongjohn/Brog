from flask.blueprints import Blueprint
import json

bp = Blueprint(
    name='anwser',
    import_name=__name__
)

@bp.route('/user/login/', methods=['POST'])
def login():
    return json.dumps({'status': 200})
from flask.blueprints import Blueprint
from flask\
    import request, session
import json
from user.models import *
import os
import user.public

bp = Blueprint(
    name='read',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/read'
)


@bp.route('/search/', methods=["GET", "POST"])
def search():
    try:
        data = json.dumps(request.get_data(as_text=True))
    except:
        pass
    return json.dumps({
        "data": ["file1", "file2", "file3"],
        "status": 200
    }), 200

from flask.blueprints import Blueprint
from flask\
    import request,session
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

@bp.route('/tags/', methods=["GET", "POST"])
@user.public.login_required
def tags():
    # 未完成
    tags_ = []
    return json.dumps(tags_)

@bp.route('/pdf/', methods=["GET", "POST"])
@user.public.login_required
def pdf():
    def stream_file_reader():
        with open(os.path.join('./files', request.values.get('filename', default='0.pdf'))) as f:
            yield f
    return 
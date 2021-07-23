from flask.blueprints import Blueprint
from flask import request, session
from werkzeug.utils import secure_filename
import json
from user.models import *
import user.public
from file.public import *
from file.models import *
import os

ALLOWED_SUFFIX = ['pdf', 'txt']

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


@bp.route('/upload/', methods=["POST"])
@user.public.login_required
def upload():
    success, failure = 0, 0
    for x in request.files:
        y = request.files[x]
        if y.filename.split('.')[-1] not in ALLOWED_SUFFIX:
            return json.dumps({'status': 500, 'reason': 'invalid file suffix', })
        y.filename = secure_filename(y.filename)
        sql_file = File(
            contributer=session['user_id'],
            filename=y.filename
        )
        db.session.add(sql_file)
        try:
            db.session.commit()
            y.save(
                os.path.join(FILE_DIR, '(' + sql_file.id + ')-' + y.filename),
                buffer_size=512
            )
            success += 1
        except:
            db.session.rollback()
            failure += 1
    return json.dumps({'status': 200, 'success': success, 'failure': failure, })

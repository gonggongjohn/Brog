from flask.blueprints import Blueprint
from flask import request, session

from werkzeug.utils import secure_filename
import json

import user.public
from user.models import *

from file.models import *
from file.public import *

import os
from random import choices

ALLOWED_SUFFIX = ['pdf', 'txt']

bp = Blueprint(
    name='file',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/file'
)


@bp.route('/tags/', methods=["GET", "POST"])
@user.public.login_required
def tags():
    # 未完成
    tags_ = []
    return json.dumps(tags_)


@bp.route('/upload/', methods=["POST", "OPTIONS"])
@user.public.login_required
def upload():
    success, crash = 0, 0
    for x in request.files:
        y = request.files[x]
        if y.filename.split('.')[-1] not in ALLOWED_SUFFIX:
            return json.dumps({'status': 500, 'reason': 'invalid file suffix', })
        y.filename = y.filename.replace(' ', '_')
        while True:
            try:
                sql_file = File(
                    contributer=session['user_id'],
                    filename=y.filename,
                    id=''.join(
                        choices(string.ascii_letters + string.digits, k=50))
                )
                db.session.add(sql_file)
                db.session.commit()
                break
            except:
                db.session.rollback()
                pass
        y.save(
            os.path.join(FILE_DIR, '(%s)-%s' %
                         (sql_file.id, sql_file.filename)),
            buffer_size=512
        )
    return json.dumps({'status': 200, 'success': success, 'crash': crash, }), 200


@bp.route('/list_all/', methods=["POST", "OPTIONS", "GET"])
@user.public.login_required
def list_all():
    return json.dumps(list(map(lambda x: {
        "id": x.id, 
        "filename": x.filename, 
        "contributer": db.session.query(User).filter_by(id=x.contributer).first().name, 
    }, db.session.query(File).all()))), 200


@bp.route('/list_collection/', methods=["POST", "OPTIONS", "GET"])
@user.public.login_required
def list_collection():
    return json.dumps([]), 200

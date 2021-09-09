from flask.blueprints import Blueprint
from flask import request, session

import json

from flask.wrappers import Response
from werkzeug.utils import send_file, send_from_directory

import user.public
from user.models import *

from file.models import *
from file.public import *

import os
from random import choices

from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor()

ALLOWED_SUFFIX = ['pdf', ]

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
        sql_file = File(
            contributor=session['user_id'],
            filename=y.filename,
            id=''.join(choices(string.ascii_letters + string.digits, k=50))
        )
        for cnt in range(10):
            try:
                db.session.add(sql_file)
                db.session.commit()
                break
            except:
                db.session.rollback()
                sql_file.id = ''.join(
                    choices(string.ascii_letters + string.digits, k=50))
        pdf_path = os.path.join(FILE_DIR, "pdf", '(%s)-%s' %
                                (sql_file.id, sql_file.filename))
        xml_path = os.path.join(FILE_DIR, "xml", '(%s)-%s' %
                                (sql_file.id, sql_file.filename.removesuffix(".pdf") + ".xml"))
        y.save(pdf_path, buffer_size=512)
        executor.submit(pdf_to_xml(pdf_path, xml_path))
    return json.dumps({'status': 200, 'success': success, 'crash': crash, }), 200


@bp.route('/list_all/', methods=["POST", "OPTIONS", "GET"])
@user.public.login_required
def list_all():
    return json.dumps(list(map(lambda x: {
        "id": x.id,
        "filename": x.filename,
        "contributor": db.session.query(User).filter_by(id=x.contributor).first().name,
    }, db.session.query(File).all()))), 200


@bp.route('/list_collection/', methods=["POST", "OPTIONS", "GET"])
@user.public.login_required
def list_collection():
    return json.dumps(list(map(lambda x: {
        "id": x.file_id,
        "filename": db.session.query(File).filter_by(id=x.file_id).first().filename,
    }, db.session.query(Collection).filter_by(user_id=session["user_id"]).all()))), 200


@bp.route('/add_collection/', methods=["GET", "POST", "OPTIONS"])
@user.public.login_required
def add_collection():
    data = json.loads(request.get_data(as_text=True))
    book_id = data["book_id"]
    user_id = session["user_id"]
    collection_obj = Collection(
        file_id=book_id,
        user_id=user_id
    )
    if db.session.query(Collection).filter_by(file_id=book_id, user_id=user_id).first():
        return json.dumps({"status": 0, }), 200
    while True:
        try:
            db.session.add(collection_obj)
            db.session.commit()
            break
        except:
            db.session.rollback()
            collection_obj.id = ''.join(
                choices(string.ascii_letters + string.digits, k=80))
    return json.dumps({"status": 200, }), 200


@bp.route('/get_pdf/', methods=["GET", "POST", "OPTIONS"])
def get_pdf():
    try:
        data = json.loads(request.get_data(as_text=True))
        book_id = data["book_id"]
    except:
        book_id = request.values.get("book_id")
    book_filename = db.session.query(File).filter_by(
        id=book_id).first().filename

    return send_file(
        path_or_file=os.path.join(
            FILE_DIR, "pdf", "(%s)-%s" % (book_id, book_filename)),
        as_attachment=True,
        download_name=book_filename,
        environ=request.environ
    )

    # book_path = os.path.join(FILE_DIR, "pdf", "(%s)-%s" %
    #                          (book_id, book_filename))
    # def read(path):
    #     with open(path, "rb") as f:
    #         if f:
    #             yield f.read(512)
    # return Response(
    #     response=read(book_path),
    #     content_type="application/octet-stream",
    #     mimetype="text/application"
    # )


@bp.route('/get_xml/', methods=["GET", "POST", "OPTIONS"])
@user.public.login_required
def get_xml():
    try:
        data = json.loads(request.get_data(as_text=True))
        book_id = data["book_id"]
    except:
        book_id = request.values.get("book_id")
    book_obj = db.session.query(File).filter_by(id=book_id).first()

    book_filename = book_obj.filename.removesuffix(book_obj.suffix)

    return send_file(
        path_or_file=os.path.join(
            FILE_DIR, "pdf", "(%s)-%s" % (book_id, book_filename)),
        as_attachment=True,
        download_name=book_filename,
        environ=request.environ
    )

    # def read(path):
    #     with open(path, "rb") as f:
    #         if f:
    #             yield f.read(512)
    # book_path = os.path.join(FILE_DIR, "xml", "(%s)-%s" %
    #                          (book_id, book_filename))
    # return Response(read(book_path), content_type="application/octet-stream", headers={"Content-Disposition": "attachment", })


@bp.route('/get_json/', methods=["GET", "POST", "OPTIONS"])
@user.public.login_required
def get_json():
    try:
        data = json.loads(request.get_data(as_text=True))
        book_id = data["book_id"]
    except:
        book_id = request.values.get("book_id")
    book_filename = db.session.query(File).filter_by(
        id=book_id).first().filename.removesuffix("pdf") + "json"

    def render(path: str) -> str:
        ret = ""
        with open(path, "r") as f:
            ret += f.read()
        return ret
    return render(os.path.join(FILE_DIR, "json",
                               "(%s)-%s" % (book_id, book_filename)))
    #    "test.json"))


@bp.route("/get_md/", methods=["GET", "POST", "OPTIONS"])
@user.public.login_required
def get_md():
    try:
        data = json.loads(request.get_data(as_text=True))
        book_id = data["book_id"]
    except:
        book_id = request.values.get("book_id")
    book_obj = db.session.query(File).filter_by(id=book_id).first()
    book_filename = book_obj.filename.removesuffix(book_obj.suffix) + "md"

    def render_to_str(path: str) -> str:
        ret = ""
        with open(path, "r") as f:
            ret += f.read()
        return ret
    
    try:
        ret = render_to_str(os.path.json(
            FILE_DIR, "md", "(%s)-%s" % (book_id, book_filename)))
        return json.dumps({
            "status": 200,
            "data": ret,
        }), 200
    except:
        return json.dumps({
            "status": 404,
            "data": "Sorry on such file",
        }), 200

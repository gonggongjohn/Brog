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

ALLOWED_SUFFIX = ['pdf', 'md', ]

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
        suffix = y.filename.split('.')[-1]
        if suffix not in ALLOWED_SUFFIX:
            return json.dumps({'status': 500, 'reason': 'invalid file suffix', })
        y.filename = y.filename.replace(' ', '_')
        sql_file = File(
            contributor=session['user_id'],
            filename=y.filename,
            id=''.join(choices(string.ascii_letters + string.digits, k=50)),
            suffix=suffix
        )
        while crash < 10:
            try:
                db.session.add(sql_file)
                db.session.commit()
                break
            except:
                crash += 1
                db.session.rollback()
                sql_file.id = ''.join(
                    choices(string.ascii_letters + string.digits, k=50))
        if suffix == 'pdf':
            pdf_path = os.path.join(FILE_DIR, "pdf", '(%s)-%s' %
                                    (sql_file.id, sql_file.filename))
            xml_path = os.path.join(FILE_DIR, "xml", '(%s)-%s' %
                                    (sql_file.id, sql_file.filename.removesuffix(".pdf") + ".xml"))
            y.save(pdf_path, buffer_size=512)
            executor.submit(pdf_to_xml(pdf_path, xml_path))
        elif suffix == 'md':
            md_path = os.path.join(FILE_DIR, "md", '(%s)-%s' %
                                   (sql_file.id, sql_file.filename))
            y.save(md_path, buffer_size=512)

            def put_to_database(word):
                from read.models import SearchWord
                sql_word = SearchWord(id=''.join(choices(string.ascii_letters + string.digits, k=80)),
                                      spelling=word, fromFile=sql_file.id, major=0)
                for x in range(5):
                    try:
                        db.session.add(sql_word)
                        db.session.commit()
                        break
                    except:
                        db.session.rollback()
                        sql_word.id = ''.join(
                            choices(string.ascii_letters + string.digits, k=80)
                        )
                return sql_word.id

            executor.submit(markdown_bold_to_link(md_path, put_to_database))
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
    book_filename = db.session.query(File).filter_by(
        id=book_id).first().filename.removesuffix("pdf") + "xml"

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


@bp.route('/get_md/', methods=["GET", "POST", "OPTIONS"])
@user.public.login_required
def get_md():
    try:
        data = json.loads(request.get_data(as_text=True))
        book_id = data["book_id"]
    except:
        book_id = request.values.get("book_id")

    try:
        book_obj = db.session.query(File).filter_by(id=book_id).first()
        book_filename = book_obj.filename.removesuffix(book_obj.suffix) + "md"
        book_path = os.path.join(FILE_DIR, "md", "(%s)-%s" %
                                 (book_id, book_filename))
    except:
        book_path = os.path.join(FILE_DIR, "md", "test.md")
        pass

    def read_str(book_path):
        ret = ""
        with open(book_path, "r") as f:
            ret = f.read()
        return ret
    return read_str(book_path), 200


@bp.route('/get_md_lines/', methods=["GET", "POST", "OPTIONS"])

def get_md_lines():
    try:
        print(request.get_data(as_text=True))
        data = json.loads(request.get_data(as_text=True))
        book_list = data["book_list"]
    except:
        book_list = request.values.get("book_list")

    def read_str(book_path):
        ret = ""
        with open(book_path, "r") as f:
            line = f.readline()
            cnt = 0
            while line and cnt <= 30:
                ret = ret + line
                cnt += 1
                line = f.readline()
        return ret

    ret = {}
    print(book_list)
    for book_id in book_list:
        try:
            book_obj = db.session.query(File).filter_by(id=book_id).first()
            book_filename = book_obj.filename
            # book_filename = book_obj.filename.removesuffix(
            #    "." + book_obj.suffix)
            print(book_filename)
            book_path = os.path.join(FILE_DIR, "md", "(%s)-%s" %
                                     (book_id, book_filename))
            ret[book_filename] = read_str(book_path)
        except Exception as e:
            print(e)
            pass
    return json.dumps({
        "data": ret,
        "status": 200
    }), 200

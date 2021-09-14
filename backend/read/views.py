from flask.blueprints import Blueprint
from flask\
    import request, session
import json
from user.models import *
import os
import user.public
from ext import db
from read.models import *
from user.models import *

bp = Blueprint(
    name='read',
    import_name=__name__,
    static_folder='static',
    template_folder='templates',
    url_prefix='/read'
)


@bp.route('/search/', methods=["GET", "POST"])
@user.public.login_required
def search():
    try:
        data = json.loads(request.get_data(as_text=True))
        word_id, file_id = data["word_id"], data["file_id"]
        wordObj = db.session.query(SearchWord).filter_by(id=word_id).first()
        otherWordObjs = db.session.query(SearchWord).filter_by(
            spelling=wordObj.spelling).all()
        user_id = session["user_id"]
        user_obj = db.session.query(User).filter_by(id=user_id).first()
        responseData = []
        for obj in otherWordObjs:
            print(obj.major == 0)
            if obj.major == 0 or obj.major == user_obj.major:
                responseData.append(obj.fromFile)
                print("Appended!")
        # responseData = list(map(lambda x: x.fromFile, list(otherWordObjs)))
    except:
        responseData = list()
    return json.dumps({
        "data": responseData,
        "status": 200
    }), 200

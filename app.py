#!/usr/bin/env python3

import os
import sys
from flask import Flask, request, Response, jsonify, render_template
from be.model.database import init_db
from be.model.route import bp
from flask_dropzone import Dropzone

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

@bp.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        file_path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
        f.save(file_path)
        # You can return a JSON response then get it on client side:
        # (see template index.html for client implementation)
        # return jsonify(uploaded_path=file_path)
    return render_template('upload.html')


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.update(
        UPLOADED_PATH=os.path.join(file_dir, 'uploads'),
        # Flask-Dropzone config:
        DROPZONE_ALLOWED_FILE_CUSTOM=True,
        # app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, .pdf, .txt'
        DROPZONE_ALLOWED_FILE_TYPE='.pdf,.txt',
        DROPZONE_MAX_FILE_SIZE=5,
        DROPZONE_MAX_FILES=30,
    )
    dropzone = Dropzone()
    dropzone.init_app(app)
    app.register_blueprint(bp)
    init_db()
    app.run()

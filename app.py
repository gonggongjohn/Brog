#!/usr/bin/env python3

import os
import sys
from flask import Flask, request, Response, jsonify, render_template
from be.model.database import init_db
from be.model.route import bp

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(bp)
    init_db()
    app.run()

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from settings import ALLOWED_HOSTS

db = SQLAlchemy()
cors = CORS(resources={r"/.*": {"origins": ALLOWED_HOSTS}})
from flask_cors import CORS
cors = CORS(resources={r"/.*": {"origins": ["http://localhost:8080"]}})

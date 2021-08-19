from flask import *
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=8080
    )
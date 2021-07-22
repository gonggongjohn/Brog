from flask import Flask


def create():
    app = Flask(__name__)
    import ext
    ext.cors.init_app(app)
    import anwser
    app.register_blueprint(anwser.bp)
    return app
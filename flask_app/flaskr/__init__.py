from flask import Flask

from flaskr.api import api_bp


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(api_bp)

    return app

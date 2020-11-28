from flask_api import FlaskAPI


def create_app():
    app = FlaskAPI(__name__)

    return app
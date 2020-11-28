from flask_api import FlaskAPI

def create_app():
    app = FlaskAPI(__name__)

    from .endpoints.create_qr import bp

    app.register_blueprint(bp)

    return app
from flask import Flask
from flask_mongoengine import MongoEngine

from .api import api
from .settings import DevSettings


def create_app(settings=DevSettings):
    app = Flask(__name__)

    app.config.from_object(settings)
    app.register_blueprint(api)

    MongoEngine(app)

    return app

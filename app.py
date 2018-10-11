from flask import Flask
from feed_api.api import api

app = Flask(__name__)

app.register_blueprint(api)

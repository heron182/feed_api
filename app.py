from flask import Flask
from .feed import api

app = Flask(__name__)

app.register_blueprint(api)

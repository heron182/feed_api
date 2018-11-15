from bson.objectid import ObjectId
from flask import Blueprint, abort, g, jsonify, request
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from pymongo import MongoClient, ReturnDocument

from .utils import bson_to_dict

api = Blueprint("api", __name__, url_prefix="/api")
auth = HTTPBasicAuth()

mongo_client = MongoClient("db", 27017)
db = mongo_client.api


@auth.verify_password
def verify_password(username, password):
    user = db.users.find_one({"email": username})
    if user and pwd_context.verify(password, user["password"]):
        g.user = user
        return True

    return False


@api.route("/feed", methods=["GET", "POST"])
@auth.login_required
def feed():
    if request.method == "GET":
        posts = db.feed.find()

        posts = bson_to_dict(posts)
        return jsonify(posts)

    elif request.method == "POST":
        document = {}

        try:
            document["author"] = request.json["author"]
            document["title"] = request.json["title"]
            document["content"] = request.json["content"]

        except KeyError:
            abort(400)

        db.feed.insert_one(document)

        return jsonify(bson_to_dict(document))


@api.route("/feed/<feed_id>/comment", methods=["POST"])
@auth.login_required
def feed_comment(feed_id):
    document = {}

    try:
        document["author"] = g.user
        document["author"].pop("password")
        document["content"] = request.json["content"]

    except KeyError:
        abort(400)

    document["_id"] = ObjectId()
    feed = db.feed.find_one_and_update(
        {"_id": ObjectId(feed_id)},
        {"$push": {"comments": document}},
        return_document=ReturnDocument.AFTER,
    )

    return jsonify(bson_to_dict(feed))


@api.route("/users", methods=["GET"])
@auth.login_required
def list_users():
    if request.method == "GET":
        users = db.users.find()

        users = bson_to_dict(users)
        return jsonify(users)


@api.route("/users", methods=["POST"])
def create_user():
    document = {}

    try:
        document["name"] = request.json["name"]
        document["email"] = request.json["email"]
        document["password"] = pwd_context.encrypt(str(request.json["password"]))

    except KeyError:
        abort(400)

    db.users.insert_one(document)

    return jsonify(bson_to_dict(document))

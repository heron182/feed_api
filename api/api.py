from bson.objectid import ObjectId
from flask import Blueprint, jsonify, request
from pymongo import MongoClient, ReturnDocument

from .utils import bson_to_dict

api = Blueprint("api", __name__, url_prefix="/api")

mongo_client = MongoClient("localhost", 27017)
db = mongo_client.api


@api.route("/feed", methods=["GET", "POST"])
def feed():
    if request.method == "GET":
        posts = db.feed.find()

        posts = bson_to_dict(posts)
        return jsonify(posts)

    elif request.method == "POST":
        document = {}

        document["author"] = request.json["author"]
        document["title"] = request.json["title"]
        document["content"] = request.json["content"]

        db.feed.insert_one(document)

        return jsonify(bson_to_dict(document))


@api.route("/feed/<feed_id>/comment", methods=["POST"])
def feed_comment(feed_id):
    document = {}

    document["author"] = request.json["author"]
    document["content"] = request.json["content"]

    document["_id"] = ObjectId()
    feed = db.feed.find_one_and_update(
        {"_id": ObjectId(feed_id)},
        {"$push": {"comments": document}},
        return_document=ReturnDocument.AFTER,
    )

    return jsonify(bson_to_dict(feed))

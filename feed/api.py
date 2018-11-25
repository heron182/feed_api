from flask import Blueprint, abort, g, jsonify, request
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context

from .models import Comment, Post, User, Author

api = Blueprint("api", __name__, url_prefix="/api")
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = User.objects.get(email=username)
    if user and pwd_context.verify(password, user["password"]):
        g.user = user
        return True

    return False


@api.route("/feed", methods=["GET", "POST"])
@auth.login_required
def feed():
    if request.method == "GET":
        return jsonify({"result": Post.objects})

    elif request.method == "POST":
        document = {}

        try:

            document["author"] = Author(name=g.user.name, email=g.user.email)
            document["title"] = request.json["title"]
            document["content"] = request.json["content"]

            post = Post.objects.create(**document)
            return jsonify({"result": post})

        except KeyError:
            abort(400)

        return jsonify({"result": post})


@api.route("/feed/<feed_id>/comment", methods=["POST"])
@auth.login_required
def feed_comment(feed_id):
    document = {}

    try:
        document["author"] = Author(name=g.user.name, email=g.user.email)
        document["content"] = request.json["content"]

    except KeyError:
        abort(400)

    comment = Comment(**document)
    post = Post.objects.get(id=feed_id)
    post.comments.append(comment)

    return jsonify({"result": post}), 201


@api.route("/users", methods=["GET"])
@auth.login_required
def list_users():
    if request.method == "GET":
        return jsonify({"result": User.objects}), 200


@api.route("/users", methods=["POST"])
def create_user():
    document = {}

    try:
        document["name"] = request.json["name"]
        document["email"] = request.json["email"]
        document["password"] = pwd_context.encrypt(str(request.json["password"]))

    except KeyError:
        abort(400)

    user = User.objects.create(**document)

    return jsonify({"result": user}), 201

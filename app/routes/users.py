from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User
from app import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

users = Blueprint("users", __name__)

@users.route("/id/<int:id>", methods=["GET"])
@jwt_required()
def UserInfo(id):
    user = User.query.filter_by(id=id).first() # WARNING

    if user:
        return jsonify({"message": "success", "name": user.name, \
                        "username": user.username, "about": user.about, \
                        "creationDate": user.creationDate, \
                        "active": user.active, "private": user.private, \
                        "following": user.FollowingCount(), \
                        "followers": user.FollowersCount()}), 201
    else:
        return jsonify({"message": "User not found"}), 404

@users.route("/username/<string:username>", methods=["GET"])
@jwt_required()
def UserInfoByUsername(username):
    user = User.query.filter_by(username=username).first() # WARNING

    if user:
        return jsonify({"message": "success", "name": user.name, \
                        "username": user.username, "about": user.about, \
                        "creationDate": user.creationDate, \
                        "active": user.active, "private": user.private, \
                        "following": user.FollowingCount(), \
                        "followers": user.FollowersCount()}), 201
    else:
        return jsonify({"message": "User not found"}), 404

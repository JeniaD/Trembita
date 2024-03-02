from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User, Role
from app import db
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

api = Blueprint("api", __name__)

@api.route("/register", methods=["POST"])
def Register():
    username = request.json.get("username")
    password = request.json.get("password")
    name = request.json.get("name")
    email = request.json.get("email")

    user = User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first()

    if user: return jsonify({"message": "Username already exists"}), 400

    userRole = Role.query.filter_by(name="registeredUser").first()
    user = User(name=name, username=username, email=email, password=generate_password_hash(password))
    user.roles.append(userRole)
    db.session.add(user)
    db.session.commit()
    
    accessToken = create_access_token(identity=username)
    return jsonify(access_token=accessToken)

@api.route("/login", methods=["POST"])
def Login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401
    
    accessToken = create_access_token(identity=username)
    return jsonify(access_token=accessToken)

@api.route("/post", methods=["POST"])
@jwt_required()
def Post():
    content = request.json.get("content")
    current_user = get_jwt_identity()
    post = Post(content=content, userID=current_user)
    db.session.add(post)
    db.session.commit()

    return jsonify({"message": "success"}), 201

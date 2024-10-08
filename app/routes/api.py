from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User, Post
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

    if user: return jsonify({"message": "User already exists"}), 400

    user = User(name=name, username=username, email=email, password=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    
    accessToken = create_access_token(identity=user)
    return jsonify(access_token=accessToken)

@api.route("/login", methods=["POST"])
def Login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401
    
    accessToken = create_access_token(identity=user)
    return jsonify(access_token=accessToken)

@api.route("/post", methods=["POST"])
@jwt_required()
def MakePost():
    content = request.json.get("content")
    current_user = get_jwt_identity()
    post = Post(content=content, ownerID=current_user)
    db.session.add(post)
    db.session.commit()

    return jsonify({"message": "success"}), 201

@api.route("/like", methods=["POST"])
@jwt_required()
def Like():
    postID = request.json.get("postID")
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first() # WARNING
    post = Post.query.filter_by(id=postID).first()

    if post:
        user.LikePost(post)

        return jsonify({"message": "success"}), 201
    else:
        return jsonify({"message": "Post not found"}), 404

@api.route("/unlike", methods=["POST"])
@jwt_required()
def Unlike():
    postID = request.json.get("postID")
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first() # WARNING
    post = Post.query.filter_by(id=postID).first()

    if post:
        user.UnlikePost(post)
        return jsonify({"message": "success"}), 201
    else:
        return jsonify({"message": "Post not found"}), 404

@api.route("/updateProfile", methods=["POST"])
@jwt_required()
def UpdateProfile():
    name = request.json.get("name")
    username = request.json.get("username")
    about = request.json.get("about")

    if not username or not name: return jsonify({"message": "Wrong data"}), 422

    user = User.query.filter_by(id=get_jwt_identity()).first()

    if not user: return jsonify({"message": "User no longer exists"}), 400 # Should users shortly after deletion be able to act for some time?
    user.name = name
    user.username = username
    user.about = about

    db.session.commit()
    
    return jsonify({"message": "success"}), 201

@api.route("/topPosts", methods=["GET"])
@jwt_required()
def TopPosts():
    page = request.args.get("page", 1, type=int)
    perPage = request.args.get("perPage", 30, type=int)

    posts = Post.query.order_by(Post.creationDate.desc()).limit(500).all().paginate(page, perPage, error_out=False) # WARNING
    posts.sort(key=lambda post: post.LikesCount, reverse=True)

    res = [{"id": post.id, "content": post.content, "creationDate": post.creationDate.strftime("%Y-%m-%d %H:%M:%S"), "likesCount": post.LikesCount} for post in posts]
    
    return jsonify(posts=res), 201

# @api.route("/trends", methods=["GET"])
# @jwt_required()
# def TopPosts():
#     posts = Post.query.order_by(Post.creationDate.desc()).limit(50).all()
#     posts.sort(key=lambda post: post.LikesCount, reverse=True)

#     res = [{"id": post.id, "content": post.content, "creationDate": post.creationDate.strftime("%Y-%m-%d %H:%M:%S"), "likesCount": post.LikesCount} for post in posts]
    
#     return jsonify(posts=res), 201

@api.route("/subscribedPosts", methods=["GET"])
@jwt_required()
def FollowersPosts():
    page = request.args.get("page", 1, type=int)
    perPage = request.args.get("perPage", 30, type=int)

    followings = User.query.get(get_jwt_identity()).following
    posts = Post.query.filter(Post.author_id.in_([user.id for user in followings])).order_by(Post.creationDate.desc()).paginate(page, perPage, error_out=False)
    posts.sort(key=lambda post: post.LikesCount, reverse=True) # WARNING: optional

    res = [{"id": post.id, "content": post.content, "creationDate": post.creationDate.strftime("%Y-%m-%d %H:%M:%S"), "likesCount": post.LikesCount} for post in posts]
    
    return jsonify(posts=res), 201

from flask import render_template, Blueprint, abort, request, jsonify, redirect, url_for
from app.models import User, Post
from flask_login import login_required, current_user
from app import db

user = Blueprint("user", __name__)

@user.route("/profile")
@login_required
def Profile():
    return render_template("profile.html")

@user.route("/trending")
@login_required
def Trends():
    return render_template("trends.html")

@user.route("/notifications")
@login_required
def Notifications():
    return render_template("notifications.html")

@user.route("/messages")
@login_required
def Messages():
    return render_template("messages.html")

@user.route("/other")
@login_required
def Other():
    return render_template("other.html")

@user.route("/profile/<username>")
def ShowProfile(username):
    username = username.replace('@', '')

    if current_user.is_authenticated and current_user.username == username: return redirect(url_for("user.Profile"))

    user = User.query.filter_by(username=username).first()
    if not user: abort(404)

    if user.private: render_template("user.html", name=user.name, username=user.username, about=user.about, private=True)
    return render_template("user.html", name=user.name, username=user.username, about=user.about, posts=user.posts.all(), private=False)

@user.route("/home")
@login_required
def Home():
    users = User.query.all()
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template("index.html", recommendedUsers=users[:5], posts=posts)

@user.route("/post", methods=["POST"])
@login_required
def MakePost():
    content = request.json.get("content")
    if not content or len(content) > 100:
        return jsonify({"message": "Октава не може бути пуста або більше ніж 100 символів"}), 400
    
    post = Post(content=content, userID=current_user.id)
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "Октава була опублікована"}), 201

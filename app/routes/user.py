from flask import render_template, Blueprint, abort, flash, request, redirect, url_for, jsonify
from app.models import User, Post
from flask_login import login_required, current_user
from app import db

user = Blueprint("user", __name__)

@user.route("/profile")
@login_required
def Profile():
    return render_template("profile.html")

@user.route("/trending") #trends
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

user.route("/profile/<username>")
def ShowProfile(username):
    username = username.replace('@', '')
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
    content = request.json.get("content") # request.form.get("content")
    if not content or len(content) > 100:
        return jsonify({"message": "Content cannot be empty or longer than 100 characters"}), 400
        # flash("Error: octave is too large")
        # abort(422)
        # return redirect(url_for("main.Home"))
    
    post = Post(content=content, userID=current_user.id)
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "Post created successfully"}), 201
    # flash("Success!")
    # return redirect(url_for("main.Home"))
    # return jsonify({'message': 'Post created successfully'}), 200

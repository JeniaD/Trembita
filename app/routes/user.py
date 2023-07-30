from flask import render_template, Blueprint, abort
from app.models import User
from flask_login import login_required, current_user

user = Blueprint("user", __name__)

@login_required
@user.route("/profile")
def Profile():
    return render_template("profile.html", name=current_user.name, \
                           username=current_user.username, about=current_user.about, posts=current_user.posts.all(), private=current_user.private)

@login_required
@user.route("/notifications")
def Notifications():
    return render_template("notifications.html")

user.route("/profile/<username>")
def ShowProfile(username):
    username = username.replace('@', '')
    user = User.query.filter_by(username=username).first()
    if not user: abort(404)

    if user.private: render_template("user.html", name=user.name, username=user.username, about=user.about, private=True)
    return render_template("user.html", name=user.name, username=user.username, about=user.about, posts=user.posts.all(), private=False)

@login_required
@user.route("/home")
def Home():
    users = User.query.all()
    return render_template("index.html", recommendedUsers=users[:5])
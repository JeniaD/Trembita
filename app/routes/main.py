from flask import render_template, Blueprint, redirect, url_for, current_app, send_from_directory
from flask_login import current_user
from app.models import User, Post

main = Blueprint("main", __name__)

@main.route("/uploads/avatars/<filename>")
def UploadedAvatar(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], "avatars/" + filename + ".jpg")

@main.route("/uploads/<filename>")
def UploadedFile(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)

@main.route("/")
def index():
    if current_user.is_authenticated: return redirect(url_for("user.Home"))
    return render_template("index.html", posts=Post.query.order_by(Post.date.desc()).all())

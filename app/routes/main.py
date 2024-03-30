from flask import render_template, Blueprint, redirect, url_for, current_app, send_from_directory, send_file
from flask_login import current_user
from app.models import User, Post
import os

main = Blueprint("main", __name__)

@main.route("/uploads/avatars/<filename>")
def UploadedAvatar(filename):
    filePath = os.path.join(current_app.config["UPLOAD_FOLDER"], f"avatars/{filename}.jpg")
    
    if os.path.exists(filePath):
        send_file(filePath, mimetype="image/jpeg")
    else:
        filePath = os.path.join(current_app.config["UPLOAD_FOLDER"], f"avatars/default.png")
        return send_file(filePath, mimetype="image/png")

    return send_from_directory(current_app.config["UPLOAD_FOLDER"], "avatars/" + filename + ".jpg")

@main.route("/uploads/<filename>")
def UploadedFile(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)

@main.route("/")
def index():
    if current_user.is_authenticated: return redirect(url_for("user.Home"))
    return redirect(url_for("auth.Login"))
    # render_template("index.html", posts=Post.query.order_by(Post.date.desc()).all())

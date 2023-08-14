from flask import render_template, Blueprint, redirect, url_for
from flask_login import current_user
from app.models import User, Post

main = Blueprint("main", __name__)

@main.route("/")
def index():
    if current_user.is_authenticated: return redirect(url_for("user.Home"))
    return render_template("index.html", posts=Post.query.order_by(Post.date.desc()).all())

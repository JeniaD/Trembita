from flask import render_template, Blueprint
from app.models import User

main = Blueprint('main', __name__)

@main.route("/profile")
def Profile():
    return render_template("profile.html")

@main.route("/notifications")
def Notifications():
    return render_template("notifications.html")

@main.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

from flask import render_template, Blueprint
from app.models import User
from flask_login import login_required, current_user

user = Blueprint("user", __name__)

@login_required
@user.route("/profile")
def Profile():
    return render_template("profile.html")

@login_required
@user.route("/notifications")
def Notifications():
    return render_template("notifications.html")

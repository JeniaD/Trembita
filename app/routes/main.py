from flask import render_template, Blueprint
from app.models import User
from flask_login import login_required, current_user

main = Blueprint("main", __name__)

@main.route("/")
@login_required
def index():
    users = User.query.all()
    return render_template("index.html", users=users[:5])

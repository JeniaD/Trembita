from flask import render_template, Blueprint
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route("/login")
def Login():
    return render_template("login.html")

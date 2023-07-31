from flask import render_template, Blueprint, redirect, url_for
from flask_login import current_user

main = Blueprint("main", __name__)

@main.route("/")
def index():
    if current_user.is_authenticated: return redirect(url_for("user.Home"))
    return render_template("index.html")

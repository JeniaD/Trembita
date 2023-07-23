from flask import render_template
from app import app
from app.models import User

@app.route("/login")
def Login():
    return render_template("login.html")

@app.route("/profile")
def Profile():
    return render_template("profile.html")

@app.route("/notifications")
def Notifications():
    return render_template("notifications.html")

@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

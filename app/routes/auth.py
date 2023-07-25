from flask import render_template, Blueprint, request, redirect, url_for, flash
from app.models import User, Role
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required
from app import db

auth = Blueprint("auth", __name__)

def CheckName(name): return len(name) > 0 and len(name) < 20
def CheckUsername(username): return len(username) > 0 and len(username) < 20
def CheckEmail(email): return len(email) > 4 and len(email) < 20 and '@' in email
def CheckPassword(password): return len(password) > 0 and len(password) < 100

@auth.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not CheckUsername(username) or not CheckPassword(password):
            flash("Please fill out all fields")
            return redirect(url_for("auth.Login"))

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Invalid credentials")
            return redirect(url_for("auth.Login"))

        login_user(user)
        return redirect(url_for("main.index"))
    return render_template("login.html")

@auth.route("/register", methods=["GET", "POST"])
def Register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not username or not email or not password:
            flash("Please fill out all fields")
            return redirect(url_for("auth.Register"))

        user = User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first()
        if user:
            flash("User already exists. Please log in")
            return redirect(url_for("auth.Login"))

        userRole = Role.query.filter_by(name="registeredUser").first()
        user = User(name=name, username=username, email=email, password=generate_password_hash(password))
        user.roles.append(userRole)
        db.session.add(user)
        db.session.commit()

        # Optional
        login_user(user)

        return redirect(url_for("main.index"))

    return render_template("login.html")

@auth.route("/logout")
@login_required
def Logout():
    logout_user()
    return redirect(url_for("main.index"))
from flask import render_template, Blueprint
from app.models import User
from flask_login import login_required, current_user

errors = Blueprint("errors", __name__)

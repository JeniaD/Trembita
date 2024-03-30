from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
from flask_babel import Babel
from flask_jwt_extended import JWTManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    import os
    app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")

    # Initialize database
    db.init_app(app)

    # Register blueprints
    from .routes.api import api as apiBlueprint
    app.register_blueprint(apiBlueprint, url_prefix="/api")

    # Add login manager
    # loginManager = LoginManager()
    # loginManager.login_view = "auth.Login"
    # loginManager.init_app(app)

    # Initialize Babel
    babel = Babel(app)

    # Initialize JWT manager
    jwt = JWTManager(app)

    from .models import User
    # @loginManager.user_loader
    # def LoadUser(userID): return User.query.get(int(userID))
    # loginManager.login_message = "Будь ласка, увійдіть для перегляду сторінки"

    @jwt.user_identity_loader
    def UserIdentityLookup(user):
        return user.id
    
    @jwt.user_lookup_loader
    def UserLookupCallback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()
    
    return app

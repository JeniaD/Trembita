from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    CORS(app)

    import os
    app.config["UPLOAD_FOLDER"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")

    # Initialize database
    db.init_app(app)

    # Register blueprints
    from .routes.api import api as apiBlueprint
    from .routes.users import users as usersBlueprint
    apiBlueprint.register_blueprint(usersBlueprint, url_prefix="/users") # WARNING url_prefix
    app.register_blueprint(apiBlueprint, url_prefix="/api")

    # Initialize JWT manager
    jwt = JWTManager(app)

    from .models import User

    @jwt.user_identity_loader
    def UserIdentityLookup(user):
        return user.id
    
    @jwt.user_lookup_loader
    def UserLookupCallback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    @app.route("/")
    def Home():
        return "Hello world"
    return app

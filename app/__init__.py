from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    # Register blueprints
    from .routes.main import main as mainBlueprint
    app.register_blueprint(mainBlueprint)
    from .routes.auth import auth as authBlueprint
    app.register_blueprint(authBlueprint)

    db.init_app(app)
    
    return app

# from flask_sqlalchemy import SQLAlchemy
# import flask_login

# # Initialize Flask app
# app = Flask(__name__)
# app.config.from_pyfile("config.py")

# # Initialize database
# db = SQLAlchemy(app)

# # Initialize login manager
# loginManager = flask_login.LoginManager()
# loginManager.init_app(app)

# from app import routes, models

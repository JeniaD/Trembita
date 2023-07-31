from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Initialize database
    db.init_app(app)

    # Register blueprints
    from .routes.main import main as mainBlueprint
    app.register_blueprint(mainBlueprint)
    from .routes.auth import auth as authBlueprint
    app.register_blueprint(authBlueprint)
    from .routes.user import user as userBlueprint
    app.register_blueprint(userBlueprint)
    from .routes.errors import errors as errorsBlueprint
    app.register_blueprint(errorsBlueprint)

    # Add login manager
    loginManager = LoginManager()
    loginManager.login_view = "auth.Login"
    loginManager.init_app(app)

    # Initialize Babel
    babel = Babel(app)

    from .models import User
    @loginManager.user_loader
    def LoadUser(userID): return User.query.get(int(userID))

    # from flask import request
    # @babel.localeselector
    # def GetLocale(): return request.accept_languages.best_match(['en', 'uk'])
    
    return app

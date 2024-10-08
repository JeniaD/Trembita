from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        # Initialize database
        db.create_all()
        # InitRoles()

        # Create admin user
        adminUser = User(name="Trembita", username="trembita", email="admin@trembita.com", password=generate_password_hash("admin"), isAdmin=True, verified=True)
        # admin_user.roles.append(admin_role)
        db.session.add(adminUser)
        db.session.commit()

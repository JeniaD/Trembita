from app import create_app, db
from app.models import InitRoles, User, Role
from werkzeug.security import generate_password_hash

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        # Initialize database
        db.create_all()
        InitRoles()

        # Create admin user
        admin_role = Role.query.filter_by(name="admin").first()
        admin_user = User(name="Trembita", username="trembita", email="admin@trembita.com", password=generate_password_hash("admin"))
        admin_user.roles.append(admin_role)
        db.session.add(admin_user)
        db.session.commit()

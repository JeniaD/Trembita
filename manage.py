from app import app, db
from app.models import InitRoles, User, Role

if __name__ == '__main__':
    with app.app_context():
        # Initialize database
        db.create_all()
        InitRoles()

        # Create admin user
        admin_role = Role.query.filter_by(name='admin').first()
        admin_user = User(username='admin', email='admin@example.com', password='adminpassword')
        admin_user.roles.append(admin_role)
        db.session.add(admin_user)
        db.session.commit()
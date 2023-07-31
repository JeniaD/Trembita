from app import db
from flask_security import UserMixin, RoleMixin
from datetime import datetime

# Association table for user roles
user_roles = db.Table(
    "user_roles",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id"))
)

# Association table for user subscribers (users subscribed to other users)
user_subscribers = db.Table(
    "user_subscribers",
    db.Column("subscriber_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    active = db.Column(db.Boolean, default=True)
    private = db.Column(db.Boolean, default=False)
    roles = db.relationship("Role", secondary=user_roles, backref=db.backref("users", lazy="dynamic"))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    about = db.Column(db.String(100), default="")
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    # subscribers = db.relationship("User", backref="author", lazy="dynamic")
    # subscribed = db.relationship("User", backref="subscriber", lazy="dynamic")

    following = db.relationship(
        "User",
        secondary=user_subscribers,
        primaryjoin=(user_subscribers.c.subscriber_id == id),
        secondaryjoin=(user_subscribers.c.user_id == id),
        backref=db.backref("subscribers", lazy="dynamic"),
        lazy="dynamic"
    )

    # followers = db.relationship(
    #     "User",
    #     secondary=user_subscribers,
    #     primaryjoin=(user_subscribers.c.user_id == id),
    #     secondaryjoin=(user_subscribers.c.subscriber_id == id),
    #     backref=db.backref("followed", lazy="dynamic"),
    #     lazy="dynamic"
    # )

    def __repr__(self):
        return f"<User {self.username}>"

class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)

    content = db.Column(db.String(100), nullable=False)
    liked = db.relationship("User", backref="liker") # likes = db.Column(db.Integer, default=0)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    userID = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"<Post {self.title}>"

class Role(db.Model, RoleMixin):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"<Role {self.name}>"

registered_user_role = Role(name="registeredUser", description="Registered User Role")
admin_role = Role(name="admin", description="Admin Role")

def InitRoles():
    roles = [
        {"name": "registeredUser", "description": "Registered User Role"},
        {"name": "admin", "description": "Admin Role"}
    ]

    for role_data in roles:
        role_name = role_data["name"]
        existing_role = Role.query.filter_by(name=role_name).first()

        if not existing_role:
            role = Role(**role_data)
            db.session.add(role)

    db.session.commit()

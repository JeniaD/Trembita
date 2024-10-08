from app import db
from datetime import datetime

followings = db.Table("followings",
    db.Column("follower_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("followed_id", db.Integer, db.ForeignKey("user.id"))
)

likes = db.Table("likes",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"))
)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    about = db.Column(db.String(100), default="")
    creationDate = db.Column(db.DateTime, default=datetime.utcnow)

    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    active = db.Column(db.Boolean, default=True)
    private = db.Column(db.Boolean, default=False)
    
    following = db.relationship("User", secondary=followings, 
                                primaryjoin=id==followings.c.follower_id,
                                secondaryjoin=id==followings.c.followed_id,
                                backref="followers")
    posts = db.relationship("Post", backref="author")
    likedPosts = db.relationship("Post", secondary=likes, backref="likers")

    verified = db.Column(db.Boolean, default=False)
    isCompany = db.Column(db.Boolean, default=False)
    isProfessional = db.Column(db.Boolean, default=False)
    isAdmin = db.Column(db.Boolean, default=False)

    def FollowersCount(self):
        return len(self.followers)
    
    def FollowingCount(self):
        return len(self.following)
    
    def IsSubscribed(self, user):
        return user in self.followers
    
    def Subscribe(self, user):
        if not self.IsSubscribed(user):
            self.following.append(user)
            return self
    
    def Unsubscribe(self, user):
        if self.IsSubscribed(user):
            self.following.remove(user)
            return self
    
    def ClearSubscribers(self):
        for user in self.following:
            self.Unsubscribe(user)
        db.session.commit()
    
    # WARNING: does post should be added, not post ID?
    def LikePost(self, post):
        if post not in self.likedPosts:
            self.likedPosts.append(post)
            db.session.commit()
    
    def UnlikePost(self, post):
        if post in self.likedPosts:
            self.likedPosts.remove(post)
            db.session.commit()

    def __repr__(self):
        return f"<User {self.username}>"

class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    ownerID = db.Column(db.Integer, db.ForeignKey("user.id")) #db.ForeignKey("author.id"))

    creationDate = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def LikesCount(self):
        return len(self.likers) #self.likers.count()

    def __repr__(self):
        return f"<Post {self.id}>"

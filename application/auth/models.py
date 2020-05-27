from application import db


class User(db.Model):

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    username = db.Column(db.String(100), nullable=False)
    pw_hash = db.Column(db.String(144), nullable=False)
    
    isAdmin = db.Column(db.Boolean, nullable=False)
    
    posts = db.relationship("Post", backref="accounts", lazy=True)

    def __init__(self, username, pw_hash, isAdmin):
        self.username = username
        self.pw_hash = pw_hash
        self.isAdmin = isAdmin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


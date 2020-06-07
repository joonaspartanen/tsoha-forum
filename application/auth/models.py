from application import db
from application.utils.helper import TimeFormatter

from sqlalchemy.sql import text


class User(db.Model):

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    username = db.Column(db.String(100), nullable=False)
    pw_hash = db.Column(db.String(144), nullable=False)

    description = db.Column(db.String(1000), nullable=True)

    is_admin = db.Column(db.Boolean, nullable=False)

    topics = db.relationship("Topic", backref="accounts", lazy=True)
    posts = db.relationship("Post", backref="accounts", lazy=True)

    def __init__(self, username, pw_hash, is_admin):
        self.username = username
        self.pw_hash = pw_hash
        self.is_admin = is_admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def get_user_with_statistics(user_id):
        stmt = text("SELECT Accounts.id, Accounts.username, Accounts.description, Accounts.is_admin, Accounts.date_created, "
                    "Post_likes.likes, Posts.posts_amount, Topics.topics_amount FROM Accounts LEFT JOIN (SELECT author_id, "
                    "COUNT(post_id) AS likes FROM Post_likes LEFT JOIN Posts ON Post_likes.post_id = Posts.id GROUP BY author_id) "
                    "AS Post_likes ON Post_likes.author_id = Accounts.id LEFT JOIN (SELECT author_id, COUNT(id) AS posts_amount "
                    "FROM Posts GROUP BY author_id) AS Posts ON Accounts.id = Posts.author_id LEFT JOIN (SELECT author_id, COUNT(id) "
                    "AS topics_amount FROM Topics GROUP BY author_id) AS Topics ON Accounts.id = Topics.author_id " 
                    "WHERE Accounts.id = :user_id;").params(user_id=user_id)

        result = db.engine.execute(stmt)
        row = result.first()
        mapped_row = [0 if item is None else item for item in row]

        return {"id": mapped_row[0], "username": mapped_row[1], "description": mapped_row[2],
                "is_admin": mapped_row[3], "date_created": TimeFormatter.get_timestamp(mapped_row[4]),
                "likes": mapped_row[5], "posts_amount": mapped_row[6], "topics_amount": mapped_row[7]}

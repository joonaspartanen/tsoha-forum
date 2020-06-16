from application import db
from application.models import Base
from application.utils.helper import TimeFormatter

from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "accounts"

    username = db.Column(db.String(100), nullable=False,
                         index=True, unique=True)
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

    @staticmethod
    def get_all_users_with_statistics():
        stmt = text("SELECT accounts.id, accounts.username, accounts.date_created, "
                    "accounts.is_admin, posts.posts_amount, topics.topics_amount "
                    "FROM accounts "
                    "LEFT JOIN (SELECT posts.author_id, COUNT(posts.id) AS posts_amount "
                    "FROM posts "
                    "GROUP BY author_id) "
                    "AS posts "
                    "ON posts.author_id = accounts.id "
                    "LEFT JOIN (SELECT topics.author_id, COUNT(topics.id) AS topics_amount "
                    "FROM topics "
                    "GROUP BY author_id) "
                    "AS topics "
                    "ON topics.author_id = accounts.id "
                    "ORDER BY accounts.username;")

        result = db.engine.execute(stmt)
        mapped_rows = [[0 if item is None else item for item in row]
                       for row in result]

        response = []

        for row in mapped_rows:
            print(row)
            response.append({"id": row[0], "username": row[1], "date_created": TimeFormatter.get_timestamp(row[2]),
                             "is_admin": row[3], "posts_amount": row[4], "topics_amount": row[5]})

        return response

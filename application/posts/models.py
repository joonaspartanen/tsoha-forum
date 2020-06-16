from application import db
from application.models import Base
from application.utils.helper import TimeFormatter
from sqlalchemy.sql import text

post_likes = db.Table("post_likes",
                      db.Column("post_id", db.Integer, db.ForeignKey(
                          "posts.id"), nullable=False, index=True),
                      db.Column("user_id", db.Integer, db.ForeignKey(
                          "accounts.id"), nullable=False, index=True)
                      )


class Post(Base):
    __tablename__ = "posts"

    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    body = db.Column(db.String(1000), nullable=False)

    liked_by_users = db.relationship("User", secondary=post_likes)

    topic_id = db.Column(db.Integer, db.ForeignKey(
        "topics.id"), nullable=False, index=True)
    topic = db.relationship("Topic", back_populates="posts")

    author_id = db.Column(db.Integer, db.ForeignKey(
        "accounts.id"), nullable=False, index=True)
    author = db.relationship("User", back_populates="posts")

    def __init__(self, body):
        self.body = body

    @staticmethod
    def find_most_liked_posts_today(amount=5):
        stmt = text("SELECT Posts.id, Posts.date_created, Posts.date_modified, "
                    "Posts.body, Post_likes.likes, Posts.topic_id, Posts.author_id, "
                    "Accounts.username FROM Posts JOIN (SELECT post_id, COUNT(post_id) AS likes "
                    "FROM Post_likes GROUP BY post_id) AS Post_likes ON Posts.id = Post_likes.post_id "
                    "JOIN Accounts ON Posts.author_id = Accounts.id WHERE date(Posts.date_created) = date('now') "
                    "ORDER BY likes DESC LIMIT :amount;").params(amount=amount)

        result = db.engine.execute(stmt)

        response = []

        for row in result:
            response.append({"id": row[0], "date_created": TimeFormatter.get_timestamp(row[1]), "date_modified": TimeFormatter.get_timestamp(row[2]),
                             "body": row[3], "likes": row[4], "topic_id": row[5], "author": {"id": row[6], "username": row[7]}, "preview": True})

        return response

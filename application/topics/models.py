from application import db
from application.tags.models import tag_topics
from application.utils.helper import TimeFormatter
from sqlalchemy.sql import text


class Topic(db.Model):
    __tablename__ = "topics"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    subject = db.Column(db.String(100), nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey(
        "accounts.id"), nullable=False)
    author = db.relationship("User", back_populates="topics")

    posts = db.relationship("Post", back_populates="topic")

    tags = db.relationship("Tag", secondary=tag_topics)

    def __init__(self, subject, author_id):
        self.subject = subject
        self.author_id = author_id

    @staticmethod
    def search_topics(subject, author):

        stmt = text("SELECT Topics.id AS topic_id, Topics.date_created, Topics.date_modified, "
                    "Topics.subject, Accounts.id AS author_id, Accounts.username AS author, Initial_posts.body "
                    "FROM Topics JOIN Accounts ON Accounts.id = Topics.author_id JOIN (SELECT topic_id, body "
                    "FROM Posts WHERE id IN(SELECT MIN(id) FROM Posts GROUP BY topic_id)) AS Initial_posts "
                    "ON Topics.id=Initial_posts.topic_id WHERE subject LIKE :subject AND author LIKE :author "
                    "ORDER BY Topics.date_created DESC;").params(subject=f"%{subject}%", author=f"%{author}%")

        result = db.engine.execute(stmt)
        print(result.keys())

        response = []

        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for row in result:
            print(row)
            response.append({"id": row[0], "date_created": TimeFormatter.get_timestamp(row[1]), "date_modified": TimeFormatter.get_timestamp(row[2]),
                             "subject": row[3], "author": {"id": row[4], "username": row[5]}, "initial_post_body": row[6]})
        return response

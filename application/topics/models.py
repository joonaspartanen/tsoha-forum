from application import db

from application.tags.models import tag_topics


class Topic(db.Model):
    __tablename__ = "topics"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    subject = db.Column(db.String(100), nullable=False)

    posts = db.relationship("Post", back_populates="topic")

    tags = db.relationship("Tag", secondary=tag_topics)

    def __init__(self, subject):
        self.subject = subject

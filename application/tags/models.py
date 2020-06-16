from application import db
from application.models import Base

tag_topics = db.Table("tag_topics",
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), nullable=False, index=True),
    db.Column("topic_id", db.Integer, db.ForeignKey("topics.id"), nullable=False, index=True)
)

class Tag(Base):
    __tablename__ = "tags"

    name = db.Column(db.String(20), nullable=False)

    topics = db.relationship("Topic", secondary=tag_topics)

    def __init__(self, name):
        self.name = name;
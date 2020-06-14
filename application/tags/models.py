from application import db

tag_topics = db.Table("tag_topics",
    db.Column("tag_id", db.Integer, db.ForeignKey("tags.id"), nullable=False, index=True),
    db.Column("topic_id", db.Integer, db.ForeignKey("topics.id"), nullable=False, index=True)
)

class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
  
    name = db.Column(db.String(20), nullable=False)

    topics = db.relationship("Topic", secondary=tag_topics)

    def __init__(self, name):
        self.name = name;
from application import db


class Topic(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    subject = db.Column(db.String(1000), nullable=False)

    posts = db.relationship('Post', back_populates='topic')

    def __init__(self, subject):
        self.subject = subject


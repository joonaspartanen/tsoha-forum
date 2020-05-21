from application import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    body = db.Column(db.String(1000), nullable=False)
    likes = db.Column(db.Integer, default=0)

    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'), nullable=False)
    topic = db.relationship('Topic', back_populates='posts')

    author_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=False)
    author = db.relationship('User', back_populates='posts')

    def __init__(self, body):
        self.body = body

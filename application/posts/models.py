from application import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    body = db.Column(db.String(1000), nullable=False)
    likes = db.Column(db.Integer, default=0)

    def __init__(self, body):
        self.body = body
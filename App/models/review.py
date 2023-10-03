from App.database import db

class Review(db.Model):
    review_time = db.Column(db.DateTime,nullable=False)
    comment = db.Column(db.Text,nullable=False)
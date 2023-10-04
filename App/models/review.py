from App.database import db

class Review(db.Model):
    review_time = db.Column(db.DateTime,nullable=False)
    comment = db.Column(db.Text,nullable=False)

    def __init__(self, reviewDate, comment):
      self.reviewDate = reviewDate
      self.comment = comment

    def toJSON(self):
      return{
        'reviewDate': self.reviewDate.strftime('%Y-%m-%d')
        'comment': self.comment
      }
      
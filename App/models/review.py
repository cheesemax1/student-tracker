from App.database import db

class Reviewd(db.Model):
  review_time = db.Column(db.DateTime, nullable = False)
  comment = db.Column(db.Text, nullable = False)

  def __init__(self, review_time, comment):
    self.review_time = review_time
    self.comment = comment

  def get_json(self):
    return{
      "Date": self.review_time,
      "Comments": self.comment
    }

      
from App.database import db
from datetime import datetime


class Review(db.Model):
  __tablename__ = 'review'

  id = db.Column(db.Integer, primary_key=True)
  student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
  lecturer_id = db.Column(db.Integer, db.ForeignKey("lecturer.id"))
  review_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
  comment = db.Column(db.Text, nullable=False)

  def __repr__(self):
    return f'<Reviewer :{self.lecturer_id.name}, Student :{self.student_id.name}>'

  def __init__(self, lecturer_id, comment):
    self.reviewDate = reviewDate
    self.comment = comment

  def toJSON(self):
    return {
        'reviewDate': self.reviewDate.strftime('%Y-%m-%d'),
        'comment': self.comment
    }

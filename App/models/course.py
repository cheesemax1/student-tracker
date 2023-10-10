from App.database import db


class Course(db.Model):
  __tablename__ = 'course'
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
  course_code = db.Column(db.String(20), unique=True, nullable=False)
  course_name = db.Column(db.String(120), nullable=False)

  def __init__(self, user_id, course_code, course_name):
    self.user_id = user_id
    self.course_code = course_code
    self.course_name = course_name

  def __repr__(self):
    return f'<Code:{self.course_code}, Lecturer :{self.user_id.name}>'

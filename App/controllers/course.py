from App.models import Course
from App.database import db


def create_course(user_id, couse_code, course_name):
  try:
    course = Course(user_id=user_id,
                    course_code=course_code,
                    course_name=course_name)
    db.session.add(course)
    db.session.commit()
  except Exception as e:
    print('error in creating course:', e)
    db.session.rollback()
    return None


def get_course_by_id(id):
  return Course.query.filter(Course.id == id).first()

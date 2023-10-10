from App.models import Course
from App.database import db
from App.models import Student
from App.models import User


def create_course(lecturer_id, course_code, course_name):
  try:
    course = Course(lecturer_id=lecturer_id,
                    course_code=course_code,
                    course_name=course_name)
    db.session.add(course)
    lecturer = User.query.get(lecturer_id)
    if not lecturer:
      return None
    lecturer.courses_teaching.append(course)
    db.session.commit()
    return course
  except Exception as e:
    print('error in creating course:', e)
    db.session.rollback()
    return None


def get_course(id):
  return Course.query.get(id)

def get_courses_by_lecturer(lecturer_id):
  return Course.query.filter_by(lecturer_id=lecturer_id).all()
def get_courses_by_student(student_id):
  return Course.query.filter_by(students=student_id).all()

def get_all_courses():
  return Course.query.all()
from App.models import Student
from App.database import db
from App.controllers.course import get_course


def create_student(name, year):
  try:
    student = Student(name=name, year=year)
    db.session.add(student)
    db.session.commit()
    return student
  except Exception as e:
    print('error creating student', e)
    db.session.rollback()
    return None


def update_student_name(name, id):
  student = get_student(id)
  if student:
    student.name = name
    db.session.add(student)
    return db.session.commit()
  return None


def update_student_year(year, id):
  student = get_student(id)
  if student:
    student.year = year
    db.session.add(student)
    return db.session.commit()
  return None


def get_student(id):
  return Student.query.get(id)


def get_all_students():
  return Student.query.all()

#Beyond Scope
# def get_students_ranked_by_karma():
#   return Student.query.order_by(Student.karma.desc()).all()


# def get_student_highest_karma(id):
#   return Student.query.filter(Student.id == id).first()


def upvote_student(id):
  student = get_student(id)
  if student:
    student.karma += 1
    db.session.add(student)
    return db.session.commit()
  return None


def downvote_student(id):
  student = get_student(id)
  if student:
    student.karma -= 1
    db.session.add(student)
    return db.session.commit()
  return None

def assign_course(student_id,course_id):
  course = get_course(course_id)
  student = get_student(student_id)
  if course and student:
    student.courses.append(course)
    db.session.add(student)
    return db.session.commit()
  return None
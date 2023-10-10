from App.models import Student
from App.database import db


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
  student = search_student_by_id(id)
  if student:
    student.name = name
    db.session.add(student)
    return db.session.commit()
  return None


def update_student_year(year, id):
  student = search_student_by_id(id)
  if student:
    student.year = year
    db.session.add(student)
    return db.session.commit()
  return None


def search_student_by_id(id):
  return Student.query.get(id)


def get_student_by_name(name):
  return Student.query.filter_by(name=name).first()


def get_students_ranked_by_karma():
  return Student.query.order_by(Student.karma.desc()).all()


def get_student_highest_karma(id):
  return Student.query.filter(Student.id == id).first()

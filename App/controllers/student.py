from App.models import Student
from App.database import db
def create_student(name,student_id):
        try:
            student = Student(name=name,student_id=student_id)
            db.session.add(student)
            db.session.commit()
            return student
        except Exception as e:
            print('error creating student', e)
            db.session.rollback()
            return None

def update_student(name,student_id):
    student = search_student_by_id(id)
    if student:
        student.student_id = student_id
        db.session.add(student)
        return db.session.commit()
    return None



def search_student_by_id(id):
    return Student.query.get(id)

def get_student_by_name(name):
    return Student.query.filter_by(name=name).first()

# def get_student_highest_karma(id):
#     return Student.query.filter(Student.id == id).first()

# def get_students_karma_above_limit(limit):
#     return Student.query.filter(Student.karma > limit).order_by(Student.karma.desc()).all()
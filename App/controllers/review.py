from App.models import Review
from App.database import db
from App.models import Student
from App.models import User


def create_review(lecturer_id, student_id, comment):
  try:
    review = Review(lecturer_id=lecturer_id,
                    student_id=student_id,
                    comment=comment)
    db.session.add(review)
    lecturer = User.query.get(lecturer_id)
    student = Student.query.get(student_id)
    if lecturer and student:
      lecturer.reviews_made.append(review)
      student.studentreviews.append(review)
      db.session.commit()
      return review
  except Exception as e:
    print("Error creating review", e)
    db.session.rollback()
    return None


def get_all_reviews():
  return Review.query.all()


def get_all_reviews_json():
  reviews = Review.query.all()
  if not reviews:
    return []
  return [review.to_json() for review in reviews]


def get_review_by_id(id):
  return Review.query.get(id)


# def get_reviews_of_student(student_id):
#   return Review.query.filter(Review.student_id == student_id)

# def get_all_review_from_user(id):
#   return Review.query.filter(Review.lecturer_id == id).all()

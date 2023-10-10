from App.models import Review
from App.database import db

def create_review(user_id, student_id, comment):
  try:
    review = Review(user_id=user_id, student_id=student_id, comment=comment)
    db.session.add(review)
    db.session.commit()
    return review
  except Exception as e:
    print ("Error creating review", e)
    db.session.rollback()
    return None

def get_all_reviews():
  return Review.query.all()

def get_all_reviews_json():
  reviews = Review.query.all()
  if not reviews:
    return []
  return [review.to_json() for review in reviews]

def get_review_by_id(review_id):
  return Review.query.get(review_id)

def get_reviews_of_student(student_id):
  return Review.query.filter_by(student_id=student_id)

def get_all_review_from_user(id):
  return Review.query.filter(Review.user_id==id).all()
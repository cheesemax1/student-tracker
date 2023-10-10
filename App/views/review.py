from flask import Blueprint, render_template, jsonify, request, send_from_directory

from App.controllers import (get_review_by_id, get_all_reviews,
                             get_reviews_of_student, get_student_by_id,
                             get_user, create_review)

review_views = Blueprint('review_views',
                         __name__,
                         template_folder='../templates')


@review_views.route('/reviews', methods=['GET'])
def get_reviews_action():
  return jsonify(get_all_reviews())


@review_views.route('/reviews', methods=['POST'])
def create_review_action():
  data = request.form
  student = get_student_by_id(data['student_id'])
  reviewer = get_user(data['reviewer_id'])
  review = create_review(student.id, reviewer.id, data['comment'])
  if review:
    return jsonify(
        {'message': f"review by {reviewer.name} created for {student.name}"})
  return jsonify({
      'error':
      f"failed to create review by {reviewer.name} for {student.name}"
  })


# @review_views.route('/reviews/<revId>', methods=['GET'])
# def get_review_action(revId):
#   review = get_review_by_id(revId)
#   if review:
#     return jsonify(review.to_json())
#   else:
#     return jsonify({"message": f'Review with id {revId} not found'}), 404

# @review_views.route('/reviews/<studId>', methods=['GET'])
# def get_student_reviews_action(studId):
#   review = get_reviews_of_student(studId)
#   if review:
#     return jsonify(review.to_json())
#   else:
#     return jsonify(
#         {"message": f'Reviews of student with if {studId} not found'}), 404

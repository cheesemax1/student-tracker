from flask import Blueprint, render_template, jsonify, request, send_from_directory

from App.controllers import (get_review_by_id, get_all_reviews,
                             get_reviews_of_student)

review_views = Blueprint('review_views',
                         __name__,
                         template_folder='../templates')


@review_views.route('/reviews', methods=['GET'])
def get_reviews_action():
  return jsonify(get_all_reviews())


@review_views.route('/reviews/<revId>', methods=['GET'])
def get_review_action(revId):
  review = get_review_by_id(revId)
  if review:
    return jsonify(review.to_json())
  else:
    return jsonify({"message": f'Review with id {revId} not found'}), 404


@review_views.route('/reviews/<studId>', methods=['GET'])
def get_student_reviews_action(studId):
  review = get_reviews_of_student(studId)
  if review:
    return jsonify(review.to_json())
  else:
    return jsonify(
        {"message": f'Reviews of student with if {studId} not found'}), 404

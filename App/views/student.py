from flask import Blueprint, render_template, jsonify, request, send_from_directory

student_views = Blueprint('student_views', __name__, template_folder='../templates')
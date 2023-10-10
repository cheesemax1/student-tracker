from flask import Blueprint, render_template, jsonify, request, send_from_directory

course_views = Blueprint('course_views', __name__, template_folder='../templates')
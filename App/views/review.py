from flask import Blueprint, render_template, jsonify, request, send_from_directory

review_views = Blueprint('review_views', __name__, template_folder='../templates')


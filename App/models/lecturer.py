from App.database import db
from .user import *

class Lecturer(User):
    __tablename__ = 'lecturer'

    id = db.Column(db.Integer, primary_key = True)
    courses_taught = db.relationship('course',backref=db.backref('lecturer'),lazy='joined')
    reviews = db.relationship('review',backref=db.backref('lecturer'),lazy='joined')

    def __repr__(self):
         return f'<Lecturer :{self.first_name, self.last_name}>'


         
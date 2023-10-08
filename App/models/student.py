from App.database import db
from .person import *
class Student(Person):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer,nullable=False)
    year = db.Column(db.Date,nullable=False,default=datetime.utcnow())
    karma = db.Column(db.Integer,default=0)
    studentreviews = db.relationship('review',backref=db.backref('student'),lazy='joined')

    def __repr__(self):
        return f'<Student :{self.first_name, self.last_name}, Year :{self.year}, Karma: {self.karma}>'

    def __init__(self,name,year,karma=0):
        self.name = name
        self.year = year
        self.karma = karma

    def toJSON(self):
        return{
            'id': self.id,
            'name': self.name,
            'year': self.year,
            'karma': self.karma
        }
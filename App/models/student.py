from App.database import db
class Student(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('Person.id'))
    student_id = db.Column(db.Integer, unique=True)
    year = db.Column(db.Date,nullable=False)
    karma = db.Column(db.Integer,default=0)
    classes = db.relationship('Class',backref='student',lazy=True)
    reviews = db.relationship('Review',backref='student',lazy=True)
    #uncertian of these relationships will need to review

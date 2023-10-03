from App.database import db

class Class(db.Model):
    class_id = db.Column(db.Integer, primary_key=True)
    lecturer_id = db.Column(db.Integer, db.ForeignKey('Lecturer.id'))
    class_name = db.Column(db.String(80), nullable=False)
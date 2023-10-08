class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    lecturer_id  = db.Column(db.Integer, db.ForeignKey("lecturer.id"))
    class_code = db.Column(db.String(20),unique=True,nullable=False)
    class_name = db.Column(db.String(120),nullable=False)

    def __repr__(self):
        return f'<Code:{self.class_code}, Lecturer :{self.lecturer_id.name}>'
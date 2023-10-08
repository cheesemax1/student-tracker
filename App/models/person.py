from App.database import db
class Person(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    
    def __init__(self, id, first_name,last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def toJSON(self):
        return {
            "id": self.id, 
            "first_name": self.first_name,
            "last_name": self.last_name
            }


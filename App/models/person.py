from App.database import db
class Person(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    name = db.Column(db.String, nullable = False)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def toJSON(self):
        return json.dumps({"id": self.id, "name": self.name})
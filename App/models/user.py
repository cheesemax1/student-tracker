from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from .person import Person

class User(Person):
    __abstract__ = True
    __tablename__ = 'user'
    username =  db.Column(db.String(120), nullable=False, unique=True)
    user_type = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    course_taught = db.relationship('Course', backref=db.backref('user'), lazy='joined')
    reviews_made = db.relationship('Review', backref=db.backref('user'), lazy = 'joined')

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.set_password(password)

    def __repr__(self):
        return f'<User {self.id} {self.username}>'

    def set_password(self, password):
       
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        
        return check_password_hash(self.password, password)

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'type': self.user_type
        }

    
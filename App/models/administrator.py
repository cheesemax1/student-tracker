from App.database import db
from .user import *

class Admin(User):
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
   
    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'type': 'administrator'
        }
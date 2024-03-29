from App.models import User
from App.database import db


def create_user(name, username, password, user_type):
  try:
    newuser = User(name=name,
                   username=username,
                   password=password,
                   user_type=user_type)
    db.session.add(newuser)
    db.session.commit()
    return newuser
  except Exception as e:
    print('error in creating user: ', e)
    db.session.rollback()
    return None


def get_user_by_username(username):
  return User.query.filter_by(username=username).first()


def get_user(id):
  return User.query.get(id)


def get_all_users():
  return User.query.all()


def get_all_users_json():
  users = User.query.all()
  if not users:
    return []
  users = [user.get_json() for user in users]
  return users


def update_user(id, username):
  user = get_user(id)
  if user:
    user.username = username
    db.session.add(user)
    return db.session.commit()
  return None

def is_admin(id):
  user = get_user(id)
  if user:
    return user.user_type == 'admin'
  return False
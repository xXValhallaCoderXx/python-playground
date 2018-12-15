from app import db

class User(db.Model):
  __tablename__ = "users"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)

  # The init method is first run the first time we create a new User
  def __init__(self, name):
      self.name = name

  # A method to represent the object when we query it
  def __repr__(self):
      return '<id {}>'.format(self.id)
from . import db
from datetime import datetime

class Todo(db.Model):
  """
  Todo Model
  """
  __tablename__ = "todos"
  __public__ = ('id', 'text', 'completed', "created_at")
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(128), nullable=False)
  completed = db.Column(db.Boolean, nullable=False)
  created_at = db.Column(db.DateTime)
  # modified_at = db.Column(db.DateTime)

  # Class constructor
  def __init__(self, text):
    """
    Class constructor
    """
    self.text = text
    self.completed = False
    self.created_at = datetime.utcnow()
    # self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_todos():
    return Todo.query.all()

  @staticmethod
  def get_one_todo(id):
    return Todo.query.get(id)

  
  def __repr(self):
    return '<id {}>'.format(self.id)
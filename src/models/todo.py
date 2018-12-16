from . import db
from datetime import datetime
from marshmallow import fields, Schema

class Todo(db.Model):
  """
  Todo Model
  """
  __tablename__ = "todos"

  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(128), nullable=False)
  completed = db.Column(db.Boolean, nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  # Class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.text = data.get('text')
    self.completed = False
    self.created_at = datetime.utcnow()
    self.modified_at = datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.utcnow()
    db.session.commit()

  @staticmethod
  def get_all_todos():
    return Todo.query.all()

  @staticmethod
  def get_one_todo(id):
    return Todo.query.get(id)

  
  def __repr(self):
    # Allows for a human printable version of the User Model
    # Just returning the ID for now
    return '<id {}>'.format(self.id)


class TodoSchema(Schema):
  """
  User Schema
  """
  id = fields.Int(dump_only=True)
  text = fields.Str(required=True)
  completed = fields.Boolean(dump_only=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
from . import db_session, Base
from datetime import datetime
from marshmallow import fields, Schema
from sqlalchemy import Column, Integer, String, Boolean, DateTime

class Todo(Base):
  """
  Todo Model
  """
  __tablename__ = "todos"

  id = Column(Integer, primary_key=True)
  text = Column(String(128), nullable=False)
  completed = Column(Boolean, nullable=False)
  created_at = Column(DateTime)
  modified_at = Column(DateTime)

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
    db_session.add(self)
    db_session.commit()

  def delete(self):
    db_session.delete(self)
    db_session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.utcnow()
    db_session.commit()

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
import unittest
import os
import json
from ..app import create_app, db

class TodoTest(unittest.TestCase):
  """
  Todo Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.todo = {
      "text": "This is a test"
    }

    with self.app.app_context():
      db.create_all()
    
  def test_todo_create(self):
    """ Test New Todo """
    res = self.client().post("/api/v1/todos/", headers={'Content-Type': 'application/json'}, data=json.dumps(self.todo))
    json_data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
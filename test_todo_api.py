import unittest
import os
import json
from src.app import create_app, db

class TodoApiTests(unittest.TestCase):

  def setUp(self):
    """
    Define Test Variables
    """
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.todo = {"test": "This is a test todo"}

    # Bind app to current context
    with self.app.app_context():
      # Create tables
      db.create_all()
  
  def test_todo_create(self):
    res = self.client().post('api/v1/todos/', data=self.todo)
    self.assertEqual(res.status_code, 200)
    self.assertIn('This is a test todo', str(res.data))

  def tearDown(self):
    # teardown all initialized variables.
    with self.app.app_context():
      # drop all tables
      db.session.remove()
      db.drop_all()


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
from flask import Flask
from .config import app_config
from .models import db

from .api.todo import todo_api as todo_blueprint # add this line

# Create App Functions
# - Takes an argument we wish to run the env in
def create_app(env_name):
  """
  Create App Factory
  """

  # Initialize App
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])
  db.init_app(app)

  app.register_blueprint(todo_blueprint, url_prefix='/api/v1/todos') # add this line
  
  return app
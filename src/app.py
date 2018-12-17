from flask import Flask
from flask_graphql import GraphQLView
from .schema import schema
from .config import app_config

# from .api.todo import todo_api as todo_blueprint # add this line

# Create App Functions
# - Takes an argument we wish to run the env in
def create_app(env_name):
  """
  Create App Factory
  """

  # Initialize App
  app = Flask(__name__)
  app.config.from_object(app_config[env_name])

  app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
  )

  # app.register_blueprint(todo_blueprint, url_prefix='/api/v1/todos') # add this line
  # @app.teardown_appcontext
  # def shutdown_session(exception=None):
  #   db_session.remove()

  return app
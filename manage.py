import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from src.app import create_app, db
from src.models.todo import Todo # Need to import the models

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

@manager.command
def reset_database():
    """
    Resets the DB
    """
    db.drop_all()
    db.create_all()
    print('DB Reset')

if __name__ == '__main__':
  manager.run()
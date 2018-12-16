# We will use Flask-Migrate (part of Alembic) to manage DB Migrations
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db

app.config.from_object(os.getenv('APP_SETTINGS'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

@manager.command
def init_database():
    """
        Initialize the DB
    """
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
  manager.run()
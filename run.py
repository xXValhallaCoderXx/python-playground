import os
from os import path
from dotenv import load_dotenv
from flask import Flask

# Create the .env file path
dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

from src.app import create_app

if __name__ == "__main__":
  env_name = os.getenv('FLASK_ENV')
  app = create_app(env_name)
  # Run App
  app.run(port=3000)
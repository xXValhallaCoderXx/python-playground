import os
from os import path
from dotenv import load_dotenv
from flask import Flask

# Create the .env file path
dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
# APP_SETTINGS is an ENV variable IE: config.DevelopmentConfig
app.config.from_object(os.getenv('APP_SETTINGS'))

print(os.getenv('APP_SETTINGS'))

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/<name>")
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
  app.run()
# This is a convention taken from Django but I think it simple to work with
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Base class which other classes will inherit and override where needed
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'MY-SECRET'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
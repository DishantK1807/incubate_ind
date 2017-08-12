import os


class BaseConfig(object):
    """Constants used throughout the application."""

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    #ENVIRONMENT = property(lambda self: self.__class__.__name__)
    MYSQL_DATABASE_DB = os.environ.get("MYSQL_DB")
    MYSQL_DATABASE_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_DATABASE_USER = os.environ.get("MYSQL_USER")
    MYSQL_DATABASE_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_DATABASE_CURSORCLASS = os.environ.get("MYSQL_CURSORCLASS")

class Development(BaseConfig):
    """Default Flask configuration inherited by all environments. Use this for development environments."""
    DEBUG = True
    TESTING = False
    SECRET_KEY = "Development"


class Testing(BaseConfig):
    TESTING = True


class Production(BaseConfig):
    DEBUG = False
    SECRET_KEY = "Production"



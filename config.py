import os
import _set_local_envs as _set_


class BaseConfig(object):
    """Constants used throughout the application."""

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    _set_.import_env_vars(BASE_DIR)
    #ENVIRONMENT = property(lambda self: self.__class__.__name__)
    MYSQL_DB = os.environ.get("MYSQL_DB")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_USER = os.environ.get("MYSQL_USER")
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_CURSORCLASS = os.environ.get("MYSQL_CURSORCLASS")

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



import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    debug_enable = os.environ.get("DEBUG")
    env_name = os.environ.get("FLASK_ENV")
    sqlalchemy_echo_enable = os.environ.get("SQLALCHEMY_ECHO")
    database_uri = os.environ.get("DATABASE_URL")
    sqlalchemy_track_notification = os.environ.get(
        "SQLALCHEMY_TRACK_MODIFICATIONS")


setup_config = Config()

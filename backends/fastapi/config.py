from distutils.debug import DEBUG
from tkinter import N
from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    """
    Settings that are most used for an app and oher resets.
    """
    APP_NAME: str = "Another todo api" 
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    """
    Settings related to the server.
    """
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    """
    Settings related to server connect.
    """
    DB_URL: str = None
    DB_NAME: str = "todos-database"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


# invoke to create default session
settings = Settings()

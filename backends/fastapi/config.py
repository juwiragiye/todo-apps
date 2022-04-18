from pydantic import BaseSettings


# class CommonSettings(BaseSettings):
#     APP_NAME: str = "Another todo API"
#     DEBUG_MODE: bool = False


# class ServerSettings(BaseSettings):
#     HOST: str = "0.0.0.0"
#     PORT: int = 8000


# class DatabaseSettings(BaseSettings):
#     DB_URL: str = ""
#     DB_NAME: str = "todo-fastapi"


# class Settings(CommonSettings, ServerSettings, DatabaseSettings):
#     pass
class Settings(BaseSettings):
    APP_NAME: str = "Another todo API"
    DB_URL: str = None
    DB_NAME: str  = None
    

settings = Settings()

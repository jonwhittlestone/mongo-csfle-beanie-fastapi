import os
from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "CustomerDB"


class ServerSettings(BaseSettings):
    pass


class DatabaseSettings(BaseSettings):
    DB_USERNAME: str = os.environ.get("MONGO_USERNAME")
    DB_PASSWORD: str = os.environ.get("MONGO_PASSWORD")
    DB_NAME: str = os.environ.get("MONGO_DATABASE")
    DB_URL: str = os.environ.get("MONGO_DATABASE")


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()

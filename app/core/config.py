import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: str

    POSTGRES_DB: str
    PATH_DB: str
    SECRET_KEY: str

    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: str

    class Config:
        env_file = ".env"

setting = Settings()

# print(setting.DATABASE_URL)
# print(setting.SECRET_KEY)
# print(setting.ALGORITHM)
# print(setting.ACCESS_TOKEN_EXPIRE_MINUTES)

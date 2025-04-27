from pydantic import ConfigDict
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DJANGO_SECRET_KEY: str

    model_config = ConfigDict(env_file = ".env")

settings = Settings()

DJANGO_SECRET_KEY = settings.DJANGO_SECRET_KEY

from pydantic import BaseSettings

class Settings(BaseSettings):
    access_key: str
    secret_key: str

    class Config:
        env_file = '.env'
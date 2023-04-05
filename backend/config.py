from pydantic import BaseSettings

class Settings(BaseSettings):
    steam_id: str
    class Config:
        env_file = ".env"
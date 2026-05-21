from pathlib import Path    
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent 

# Here I define the environment variables that will match the .env file.
class Settings(BaseSettings):
    app_name: str
    app_version: str
    environment: str
    database_url: str


    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env") # to connect the settings to the actual .env file.


settings = Settings ()
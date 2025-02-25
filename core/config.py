import os
import secrets
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Custom Integration - Task Prioritizer"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "Automatically notify slack team members of High priority tasks from jira"
    API_PREFIX: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = False
    TESTING: bool = False
    TELEX_WEBHOOK_URL: str = os.getenv("TELEX_WEBHOOK_URL", "")


settings = Settings()

from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import Field

class Settings(BaseSettings):

    OPENAI_API_KEY: str = Field(default=f"")
    model_config = SettingsConfigDict(env_file='./llama/.env', env_file_encoding='utf-8', extra='ignore')







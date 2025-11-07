from pydantic_settings import BaseSettings
from pydantic import Field
from functools import lru_cache


class Config(BaseSettings):

    # Database config
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # Security config
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = Field(..., env="ALGORITHM")
    ACCES_TOKEN_EXPIRE_MINUTES: int = Field(
        default=60, env="ACCES_TOKEN_EXPIRE_MINUTES"
    )

    # General app config
    APP_NAME: str = Field(default="Runik API")
    DEBUG: bool = Field(default=True)
    API_V1_STR: str = Field(default="/api/v1")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Cache config. Avoid .env reload
@lru_cache
def get_config():
    return Config()


# Global instance
config = get_config()

from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    META_ADS_ACCESS_TOKEN: str = Field(..., env="META_ADS_ACCESS_TOKEN")
    META_AD_ACCOUNT_ID: str = Field(..., env="META_AD_ACCOUNT_ID")
    META_APP_ID: str = Field(..., env="META_APP_ID")
    API_VERSION: str = "v21"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

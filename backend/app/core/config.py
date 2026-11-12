from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    PROJECT_NAME: str
    DEBUG: bool
    CORS_ORIGINS: list

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

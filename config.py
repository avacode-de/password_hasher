from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    @property
    def DATABASE_URL_pysqlite(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"sqlite+pysqlite:///sa.db"

settings = Settings()
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    base_directory: Path = Path(__file__).resolve().parent.parent
    app_name: str
    debug_mode: bool

    # Database configuration
    database_dialect: str
    database_host: str
    database_port: str
    database_name: str
    database_user: str
    database_password: str

    model_config = SettingsConfigDict(
        env_file=base_directory / ".env",
        env_file_encoding="utf-8",
    )


settings = Settings()  # type: ignore

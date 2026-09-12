from typing import Annotated

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class ApiSettings(BaseSettings):
    cors_allowed_origins: Annotated[list[str], NoDecode] = []

    # Port the production server (run.py) binds to.
    port: int = 8000

    # Wall-clock cap on handling a single request, regardless of what's slow
    # inside it (e.g. a hung DB call). Enforced by RequestTimeoutMiddleware.
    request_timeout_seconds: float = 30
    # How long an idle keep-alive connection stays open between requests.
    keep_alive_timeout_seconds: int = 5
    # How long in-flight requests get to finish when the server receives
    # SIGTERM (e.g. `docker stop`) before it's killed outright.
    graceful_shutdown_timeout_seconds: int = 30

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    @field_validator("cors_allowed_origins", mode="before")
    @classmethod
    def split_origins(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value


api_settings = ApiSettings()

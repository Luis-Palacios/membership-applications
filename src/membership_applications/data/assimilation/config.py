from typing import Literal

from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: Literal["local", "staging", "production"] = "local"
    debug: bool = True

    assimilation_database_url: AnyUrl

    # Time to establish a new connection to SQL Server before giving up.
    db_connect_timeout_seconds: int = 5
    # Time a single query is allowed to run before SQL Server aborts it.
    db_query_timeout_seconds: int = 30
    # Time a request waits for a free connection from the pool before raising.
    db_pool_timeout_seconds: int = 30
    # Max age of a pooled connection before it's discarded and reconnected,
    # so we never hand out a connection SQL Server has silently dropped.
    db_pool_recycle_seconds: int = 1800

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

settings = Settings()
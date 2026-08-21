from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings

ASSIMILATION_DATABASE_URL = str(settings.assimilation_database_url)

# Shared thread-safe connection pool engine
engine: Engine = create_engine(ASSIMILATION_DATABASE_URL, echo=settings.debug)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass

from sqlalchemy import Engine, create_engine

from .config import settings

ASSIMILATION_DATABASE_URL = str(settings.assimilation_database_url)

def init_engine() -> Engine:
    engine = create_engine(ASSIMILATION_DATABASE_URL, echo=settings.debug)
    return engine

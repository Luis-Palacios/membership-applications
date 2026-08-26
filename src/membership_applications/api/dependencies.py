from collections.abc import Generator
from typing import Any

from sqlalchemy.orm import Session

from membership_applications.data.assimilation.database import SessionLocal


def get_assimilation_db() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()

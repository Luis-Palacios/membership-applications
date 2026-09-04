from datetime import datetime

from pydantic import BaseModel


class PersonEventSchema(BaseModel):
    event_id: int
    person_id: int
    event_name: str
    event_date: datetime
    event_type_name: str
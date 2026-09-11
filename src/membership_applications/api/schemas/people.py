from datetime import datetime

from membership_applications.api.schemas.base import PascalModel


class PersonEventSchema(PascalModel):
    event_id: int
    person_id: int
    event_name: str
    event_date: datetime
    event_type_name: str
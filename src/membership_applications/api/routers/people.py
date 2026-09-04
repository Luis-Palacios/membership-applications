from typing import TYPE_CHECKING

from fastapi import APIRouter

from membership_applications.api.dependencies import SessionDep
from membership_applications.api.schemas.people import PersonEventSchema
from membership_applications.data.assimilation.models.person.services import get_person_events

if TYPE_CHECKING:
    from collections.abc import Sequence

    from membership_applications.data.assimilation.models.person.results import PersonEventResult

router = APIRouter(prefix="/people", tags=["people"])


@router.get("/{person_id}/events", description="Retrieve all events associated with a given person.")
def get_events(person_id: int, db: SessionDep) -> list[PersonEventSchema]:
    person_events: Sequence[PersonEventResult] = get_person_events(session=db, person_id=person_id)
    mapped_person_events = [
        PersonEventSchema(
            event_id=event.event_id,
            person_id=event.person_id,
            event_name=event.event_name,
            event_date=event.event_date,
            event_type_name=event.event_type_name,
        )
        for event in person_events
    ]
    return mapped_person_events

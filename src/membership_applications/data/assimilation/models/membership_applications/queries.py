from datetime import datetime

from sqlalchemy import Select, select

from ..person.person import Person
from .membership_application import MembershipApplication


def get_recently_generated_membership_applications_query(
    start_date: datetime, end_date: datetime
) -> Select[tuple[int, int, datetime, datetime | None, str, str]]:
    """
    Get all membership applications generated between the specified start and end dates.
    """
    return (
        select(
            MembershipApplication.id,
            MembershipApplication.person_id,
            MembershipApplication.generated_date,
            MembershipApplication.fulfilment_date,
            Person.first_name,
            Person.last_name,
        )
        .join(Person.membership_applications)
        .where(MembershipApplication.generated_date.between(start_date, end_date))
        .order_by(MembershipApplication.generated_date.desc())
    )


most_recent_membership_application_query: Select[tuple[datetime, int]] = (
    select(MembershipApplication.generated_date, MembershipApplication.id)
    .order_by(MembershipApplication.generated_date.desc())
    .limit(limit=1)
)

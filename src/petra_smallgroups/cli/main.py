from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING

from petra_smallgroups.data.assimilation.database import SessionLocal
from petra_smallgroups.data.assimilation.models.membership_applications.queries import (
    get_recently_generated_membership_applications_query,
    most_recent_membership_application_query,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.engine.row import Row

    from petra_smallgroups.data.assimilation.models.membership_applications import (
        MembershipApplication,
    )


def get_current_membership_applications() -> None:
    """
    Get all current membership applications from the database.
    """

    with SessionLocal() as s:
        most_recent_membership_application_date: datetime = datetime.now(tz=timezone.utc)

        most_recent_membership_application: Row[tuple[datetime, int]] | None = s.execute(
            statement=most_recent_membership_application_query
        ).first()
        if most_recent_membership_application is not None:
            most_recent_membership_application_date = most_recent_membership_application[0]
        start_date: datetime = most_recent_membership_application_date - timedelta(days=30)

        membership_applications: Sequence[MembershipApplication] = s.scalars(
            statement=get_recently_generated_membership_applications_query(
                start_date=start_date, end_date=most_recent_membership_application_date
            )
        ).all()
        print(
            "Found "
            f"{len(membership_applications)} membership applications generated "
            f"between {start_date} and {most_recent_membership_application_date}."
        )
        print("Membership applications:")
        for membership_application in membership_applications:
            print(membership_application)


if __name__ == "__main__":
    get_current_membership_applications()

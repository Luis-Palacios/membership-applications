from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING, NamedTuple

from petra_smallgroups.data.assimilation.query_helpers import first_as

from .queries import (
    get_recently_generated_membership_applications_query,
    most_recent_membership_application_query,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from sqlalchemy.orm import Session

    from .membership_application import MembershipApplication

DEFAULT_RECENT_WINDOW = timedelta(days=30)


@dataclass(frozen=True)
class RecentMembershipApplications:
    applications: Sequence[MembershipApplication]
    start_date: datetime
    end_date: datetime


class MostRecentMembershipApplication(NamedTuple):
    generated_date: datetime
    id: int


def get_recent_membership_applications(
    session: Session, window: timedelta = DEFAULT_RECENT_WINDOW
) -> RecentMembershipApplications:
    """
    Get membership applications generated within `window` of the most recently
    generated application (falls back to now if there are none yet).
    """
    end_date: datetime = datetime.now(tz=timezone.utc)
    most_recent = first_as(
        session, most_recent_membership_application_query, cls=MostRecentMembershipApplication
    )
    if most_recent is not None:
        end_date = most_recent.generated_date
    start_date: datetime = end_date - window

    applications: Sequence[MembershipApplication] = session.scalars(
        statement=get_recently_generated_membership_applications_query(
            start_date=start_date, end_date=end_date
        )
    ).all()
    return RecentMembershipApplications(applications=applications, start_date=start_date, end_date=end_date)

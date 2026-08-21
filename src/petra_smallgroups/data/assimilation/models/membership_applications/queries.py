from datetime import datetime

from sqlalchemy import Select, select

from .membership_application import MembershipApplication


def get_recently_generated_membership_applications_query(
    start_date: datetime, end_date: datetime
) -> Select[tuple[MembershipApplication]]:
    """
    Get all membership applications generated between the specified start and end dates.
    """
    return (
        select(MembershipApplication)
        .where(MembershipApplication.generated_date.between(cleft=start_date, cright=end_date))
        .order_by(MembershipApplication.generated_date.desc())
    )


most_recent_membership_application_query: Select[tuple[datetime, int]] = (
    select(MembershipApplication.generated_date, MembershipApplication.id)
    .order_by(MembershipApplication.generated_date.desc())
    .limit(limit=1)
)

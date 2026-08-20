from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.engine.result import Result

    from petra_smallgroups.data.src.data.assimilation.models import (
        MembershipApplication,
    )


from petra_smallgroups.data.src.data.assimilation import SessionLocal
from petra_smallgroups.data.src.data.assimilation.models.membership_applications import (
    queries,
)


def get_current_membership_applications() -> None:
    """
    Get all current membership applications from the database.
    """

    with SessionLocal() as s:
        result: Result[tuple[MembershipApplication]] = s.execute(
            queries.recent_membership_applications
        )
        for row in result:
            print(
                f"Application ID: {row.MembershipApplication.id}, Token: {row.MembershipApplication.token}"
            )


if __name__ == "__main__":
    get_current_membership_applications()

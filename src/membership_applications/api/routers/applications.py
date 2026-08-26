from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from membership_applications.api.dependencies import get_assimilation_db
from membership_applications.api.schemas.applications import (
    ApplicationApproval,
    ApplicationRejection,
    ApplicationStatus,
    MembershipApplicationBase,
)
from membership_applications.data.assimilation.models.membership_applications.services import (
    get_recent_membership_applications,
)

router = APIRouter(prefix="/applications", tags=["applications"])


@router.get("/recents", name="get_recent_applications", description="Get recent membership applications")
async def get_recent_applications(
    db: Annotated[Session, Depends(get_assimilation_db)], status: ApplicationStatus | None = None
) -> list[MembershipApplicationBase]:
    result = get_recent_membership_applications(db)
    # TODO: Implement status filter
    applications: list[MembershipApplicationBase] = [
        MembershipApplicationBase(
            application_id=membership_application.id,
            person_id=membership_application.person_id,
            person_full_name=membership_application.first_name + " " + membership_application.last_name,
            generated_date=membership_application.generated_date,
            fulfilment_date=membership_application.fulfilment_date,
            is_fulfilled=membership_application.fulfilment_date is not None,
        )
        for membership_application in result.applications
    ]
    return applications


@router.post("/approve", name="approve_application", description="Approve a membership application")
async def approve_application(application: ApplicationApproval) -> dict[str, str]:
    return {
        "message": (
            f"Application {application.application_id} approved with comments: "
            f"{application.approval_comments}"
        )
    }


@router.post("/reject", name="reject_application", description="Reject a membership application")
async def reject_application(application: ApplicationRejection) -> dict[str, str]:
    return {
        "message": (
            f"Application {application.application_id} rejected for reason: {application.rejected_reason}"
        )
    }


@router.get("/{application_id}")
async def get_application(application_id: int) -> dict[str, str]:
    return {"message": f"Application ID: {application_id}"}

from collections.abc import Generator
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Annotated, Any

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session

from petra_smallgroups.data.assimilation.database import SessionLocal
from petra_smallgroups.data.assimilation.models.membership_applications.queries import (
    get_recently_generated_membership_applications_query,
    most_recent_membership_application_query,
)

app = FastAPI()


def get_assimilation_db() -> Generator[Session, Any, None]:
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def startup_event() -> None:
    print("Starting up the Membership Applications API...")


class ApplicationStatus(str, Enum):
    pending = "Pending"
    ready_to_review = "Ready to Review"
    approved = "Approved"


class ApplicationBase(BaseModel):
    application_id: int
    person_id: int
    person_full_name: str
    generated_date: datetime
    fulfilment_date: datetime | None = None
    is_fulfilled: bool


class BaseApplicationManagement(BaseModel):
    application_id: int
    user_id: int


class ApplicationApproval(BaseApplicationManagement):
    approval_comments: str = ""

    model_config = {
        "schema_extra": {"example": {"application_id": 1, "user_id": 123, "approval_comments": "Looks good"}}
    }


class ApplicationRejection(BaseApplicationManagement):
    rejected_reason: str = ""
    model_config = {
        "schema_extra": {
            "example": {"application_id": 1, "user_id": 123, "rejected_reason": "Incomplete information"}
        }
    }


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the Membership Applications API!"}


@app.get(
    "/applications/recents", name="get_recent_applications", description="Get recent membership applications"
)
async def get_recent_applications(
    db: Annotated[Session, Depends(get_assimilation_db)], status: ApplicationStatus | None = None
) -> list[ApplicationBase]:
    most_recent_membership_application_date: datetime = datetime.now(tz=timezone.utc)
    most_recent_membership_application = db.execute(
        statement=most_recent_membership_application_query
    ).first()
    if most_recent_membership_application is not None:
        most_recent_membership_application_date = most_recent_membership_application[0]
    start_date: datetime = most_recent_membership_application_date - timedelta(days=30)
    # TODO: Implement status filter
    membership_applications = db.scalars(
        statement=get_recently_generated_membership_applications_query(
            start_date=start_date, end_date=most_recent_membership_application_date
        )
    )
    applications: list[ApplicationBase] = [
        ApplicationBase(
            application_id=membership_application.id,
            person_id=membership_application.person_id,
            person_full_name="",
            generated_date=membership_application.generated_date,
            fulfilment_date=membership_application.fulfilment_date,
            is_fulfilled=membership_application.fulfilment_date is not None,
        )
        for membership_application in membership_applications
    ]
    return applications


@app.post("/applications/approve", name="approve_application", description="Approve a membership application")
async def approve_application(application: ApplicationApproval) -> dict[str, str]:
    return {
        "message": (
            f"Application {application.application_id} approved with comments: "
            f"{application.approval_comments}"
        )
    }


@app.post("/applications/reject", name="reject_application", description="Reject a membership application")
async def reject_application(application: ApplicationRejection) -> dict[str, str]:
    return {
        "message": (
            f"Application {application.application_id} rejected for reason: {application.rejected_reason}"
        )
    }


@app.get("/applications/{application_id}")
async def get_application(application_id: int) -> dict[str, str]:
    return {"message": f"Application ID: {application_id}"}

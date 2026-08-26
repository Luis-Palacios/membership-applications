from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class ApplicationStatus(str, Enum):
    pending = "Pending"
    ready_to_review = "Ready to Review"
    approved = "Approved"


class MembershipApplicationBase(BaseModel):
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
        "json_schema_extra": {
            "example": {"application_id": 1, "user_id": 123, "approval_comments": "Looks good"}
        }
    }


class ApplicationRejection(BaseApplicationManagement):
    rejected_reason: str = ""
    model_config = {
        "json_schema_extra": {
            "example": {"application_id": 1, "user_id": 123, "rejected_reason": "Incomplete information"}
        }
    }

from sqlalchemy import select

from .membership_application import MembershipApplication

recent_membership_applications = select(MembershipApplication).limit(10)

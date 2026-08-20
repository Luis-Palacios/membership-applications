from sqlalchemy import select

from petra_smallgroups.data.src.data.assimilation.models import MembershipApplication

recent_membership_applications = select(MembershipApplication).limit(10)

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column

from petra_smallgroups.data.assimilation.database import Base


class MembershipApplication(Base):
    __tablename__ = "MemberShipApplications"

    id: Mapped[int] = mapped_column(primary_key=True, name="Id", autoincrement=True)
    token: Mapped[str] = mapped_column(name="Token")
    person_id: Mapped[int] = mapped_column(name="PersonId")
    generated_date: Mapped[datetime] = mapped_column(DateTime,name="GeneratedDate")
    fulfilment_date: Mapped[datetime] = mapped_column(DateTime, name="FulfilmentDate", nullable=True)
    life_before: Mapped[str] = mapped_column(name="LifeBefore")
    conversion: Mapped[str] = mapped_column(name="Conversion")
    life_after: Mapped[str] = mapped_column(name="LifeAfter")

    def __repr__(self) -> str:
        return f"MembershipApplication(id={self.id}, token={self.token})"

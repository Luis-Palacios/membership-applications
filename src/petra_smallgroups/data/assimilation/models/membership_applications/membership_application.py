from sqlalchemy.orm import Mapped, mapped_column

from petra_smallgroups.data.assimilation.database import Base


class MembershipApplication(Base):
    __tablename__ = "MemberShipApplications"

    id: Mapped[int] = mapped_column(primary_key=True, name="Id", autoincrement=True)
    token: Mapped[str] = mapped_column(name="Token")
    person_id: Mapped[int] = mapped_column(name="PersonId")

    def __repr__(self) -> str:
        return f"MembershipApplication(id={self.id}, token={self.token})"

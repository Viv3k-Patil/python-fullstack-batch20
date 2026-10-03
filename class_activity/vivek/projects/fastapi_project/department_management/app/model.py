
from app.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Department(Base):

    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        primary_key = True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable = True
    )


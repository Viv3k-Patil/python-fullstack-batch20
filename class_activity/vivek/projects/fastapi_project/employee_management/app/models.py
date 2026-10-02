from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Department(Base):

    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        primary_key = True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable =False
    )

class Employee(Base):

    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(
        primary_key = True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable =False
    )
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False
    )
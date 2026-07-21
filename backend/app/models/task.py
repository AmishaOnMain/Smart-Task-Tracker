from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

from sqlalchemy import Enum 
import enum


class TaskStatus(str,enum.Enum):
    TODO= "TODO"
    IN_PROGRESS= "IN_PROGRESS"
    COMPLETED= "COMPLETED"
    CANCELLED= "CANCELLED"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    category: Mapped[str] = mapped_column(
        String(100),
        default="Miscellaneous",
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        default="Medium",
    )

    estimated_duration: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    deadline: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    completed: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    user = relationship("User", backref="tasks")

    status: Mapped[TaskStatus]= mapped_column(
        Enum(TaskStatus),
        default= TaskStatus.TODO,
        nullable= False,
    )
   

    routine_frequency: Mapped[str | None] = mapped_column(
    String(20),
    nullable=True,
    )
    is_routine: Mapped[bool] = mapped_column(
    Boolean,
    default=False,
    )

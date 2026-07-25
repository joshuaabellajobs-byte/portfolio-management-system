from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)

    job_title = Column(String(150), nullable=False)

    company = Column(String(150), nullable=False)

    employment_type = Column(String(50), nullable=False)

    location = Column(String(150), nullable=True)

    start_date = Column(Date, nullable=False)

    end_date = Column(Date, nullable=True)

    is_current = Column(Boolean, nullable=False, default=False)

    description = Column(Text, nullable=True)

    display_order = Column(Integer, nullable=False, default=0)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    owner = relationship(
        "User",
        back_populates="experiences",
    )
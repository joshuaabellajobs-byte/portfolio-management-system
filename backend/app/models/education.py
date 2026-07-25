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


class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)

    school = Column(String(200), nullable=False)
    degree = Column(String(150), nullable=False)
    field_of_study = Column(String(150), nullable=True)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)

    is_current = Column(Boolean, default=False, nullable=False)

    description = Column(Text, nullable=True)

    display_order = Column(Integer, default=0, nullable=False)

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
        back_populates="educations",
    )
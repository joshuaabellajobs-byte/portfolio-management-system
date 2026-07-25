from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    level = Column(
        Enum(
            "Beginner",
            "Intermediate",
            "Advanced",
            "Expert",
            name="skill_level",
        ),
        nullable=False,
        default="Beginner",
    )

    category = Column(String(100), nullable=False)

    icon = Column(String(255), nullable=True)

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
        back_populates="skills",
    )
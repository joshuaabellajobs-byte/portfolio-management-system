from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(150), nullable=False)
    headline = Column(String(200), nullable=True)
    bio = Column(Text, nullable=True)

    phone = Column(String(50), nullable=True)
    location = Column(String(150), nullable=True)

    github_url = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    portfolio_url = Column(String(255), nullable=True)

    profile_image = Column(String(255), nullable=True)
    resume_file = Column(String(255), nullable=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
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
        back_populates="profile",
    )
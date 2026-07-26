from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(
    String(50),
    unique=True,
    nullable=False,
    index=True,
    )

    email = Column(String(100), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


    is_public = Column(
        Boolean,
        default=True,
        nullable=False,
    )



    projects = relationship(
    "Project",
    back_populates="owner",
    cascade="all, delete-orphan",
    )

    skills = relationship(
    "Skill",
    back_populates="owner",
    cascade="all, delete-orphan",
    )

    experiences = relationship(
    "Experience",
    back_populates="owner",
    cascade="all, delete-orphan",
    )

    educations = relationship(
    "Education",
    back_populates="owner",
    cascade="all, delete-orphan",
    )

    certificates = relationship(
    "Certificate",
    back_populates="owner",
    cascade="all, delete-orphan",
    )

    profile = relationship(
    "Profile",
    back_populates="owner",
    uselist=False,
    cascade="all, delete-orphan",
    )
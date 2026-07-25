from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), nullable=False)
    issuing_organization = Column(String(200), nullable=False)

    issue_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=True)

    credential_id = Column(String(150), nullable=True)
    credential_url = Column(String(500), nullable=True)

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
        back_populates="certificates",
    )
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CertificateBase(BaseModel):
    name: str
    issuing_organization: str

    issue_date: date
    expiration_date: Optional[date] = None

    credential_id: Optional[str] = None
    credential_url: Optional[str] = None

    display_order: int = 0


class CertificateCreate(CertificateBase):
    pass


class CertificateUpdate(BaseModel):
    name: Optional[str] = None
    issuing_organization: Optional[str] = None

    issue_date: Optional[date] = None
    expiration_date: Optional[date] = None

    credential_id: Optional[str] = None
    credential_url: Optional[str] = None

    display_order: Optional[int] = None


class CertificateResponse(CertificateBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
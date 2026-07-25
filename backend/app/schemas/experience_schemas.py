from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ExperienceBase(BaseModel):
    job_title: str
    company: str
    employment_type: str
    location: Optional[str] = None

    start_date: date
    end_date: Optional[date] = None

    is_current: bool = False

    description: Optional[str] = None

    display_order: int = 0


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceUpdate(BaseModel):
    job_title: Optional[str] = None
    company: Optional[str] = None
    employment_type: Optional[str] = None
    location: Optional[str] = None

    start_date: Optional[date] = None
    end_date: Optional[date] = None

    is_current: Optional[bool] = None

    description: Optional[str] = None

    display_order: Optional[int] = None


class ExperienceResponse(ExperienceBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
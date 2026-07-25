from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class SkillBase(BaseModel):
    name: str
    level: str = "Beginner"
    category: str
    icon: Optional[str] = None
    display_order: int = 0


class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    name: Optional[str] = None
    level: Optional[str] = None
    category: Optional[str] = None
    icon: Optional[str] = None
    display_order: Optional[int] = None


class SkillResponse(SkillBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ProfileBase(BaseModel):
    full_name: str
    headline: str | None = None
    bio: str | None = None

    phone: str | None = None
    location: str | None = None

    github_url: str | None = None
    linkedin_url: str | None = None
    portfolio_url: str | None = None

    profile_image: str | None = None
    resume_file: str | None = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(BaseModel):
    full_name: str | None = None
    headline: str | None = None
    bio: str | None = None

    phone: str | None = None
    location: str | None = None

    github_url: str | None = None
    linkedin_url: str | None = None
    portfolio_url: str | None = None

    profile_image: str | None = None
    resume_file: str | None = None


class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
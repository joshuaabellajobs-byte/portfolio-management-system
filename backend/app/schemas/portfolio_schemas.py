from pydantic import BaseModel, ConfigDict

from app.schemas.profile_schemas import ProfileResponse
from app.schemas.project_schemas import ProjectResponse
from app.schemas.skill_schemas import SkillResponse
from app.schemas.experience_schemas import ExperienceResponse
from app.schemas.education_schemas import EducationResponse
from app.schemas.certificate_schemas import CertificateResponse


class PortfolioResponse(BaseModel):
    profile: ProfileResponse
    projects: list[ProjectResponse]
    skills: list[SkillResponse]
    experiences: list[ExperienceResponse]
    educations: list[EducationResponse]
    certificates: list[CertificateResponse]

    model_config = ConfigDict(from_attributes=True)
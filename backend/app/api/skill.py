from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.skill_schemas import (
    SkillCreate,
    SkillResponse,
    SkillUpdate,
)
from app.services.skill_service import SkillService


router = APIRouter(
    prefix="/skills",
    tags=["Skills"],
)


@router.post(
    "",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_skill(
    skill: SkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SkillService.create_skill(
        db=db,
        skill=skill,
        current_user=current_user,
    )


@router.get(
    "",
    response_model=List[SkillResponse],
)
def get_skills(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SkillService.get_skills(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{skill_id}",
    response_model=SkillResponse,
)
def get_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SkillService.get_skill(
        db=db,
        skill_id=skill_id,
        current_user=current_user,
    )


@router.put(
    "/{skill_id}",
    response_model=SkillResponse,
)
def update_skill(
    skill_id: int,
    skill: SkillUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SkillService.update_skill(
        db=db,
        skill_id=skill_id,
        skill_data=skill,
        current_user=current_user,
    )


@router.delete(
    "/{skill_id}",
)
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return SkillService.delete_skill(
        db=db,
        skill_id=skill_id,
        current_user=current_user,
    )
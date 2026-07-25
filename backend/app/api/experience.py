from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.experience_schemas import (
    ExperienceCreate,
    ExperienceResponse,
    ExperienceUpdate,
)
from app.services.experience_service import ExperienceService


router = APIRouter(
    prefix="/experiences",
    tags=["Experiences"],
)


@router.post(
    "",
    response_model=ExperienceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_experience(
    experience: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ExperienceService.create_experience(
        db=db,
        experience=experience,
        current_user=current_user,
    )


@router.get(
    "",
    response_model=List[ExperienceResponse],
)
def get_experiences(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ExperienceService.get_experiences(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{experience_id}",
    response_model=ExperienceResponse,
)
def get_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ExperienceService.get_experience(
        db=db,
        experience_id=experience_id,
        current_user=current_user,
    )


@router.put(
    "/{experience_id}",
    response_model=ExperienceResponse,
)
def update_experience(
    experience_id: int,
    experience: ExperienceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ExperienceService.update_experience(
        db=db,
        experience_id=experience_id,
        experience_data=experience,
        current_user=current_user,
    )


@router.delete(
    "/{experience_id}",
)
def delete_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ExperienceService.delete_experience(
        db=db,
        experience_id=experience_id,
        current_user=current_user,
    )
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.education_schemas import (
    EducationCreate,
    EducationResponse,
    EducationUpdate,
)
from app.services.education_service import EducationService


router = APIRouter(
    prefix="/educations",
    tags=["Educations"],
)


@router.post(
    "",
    response_model=EducationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_education(
    education: EducationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EducationService.create_education(
        db=db,
        education=education,
        current_user=current_user,
    )


@router.get(
    "",
    response_model=List[EducationResponse],
)
def get_educations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EducationService.get_educations(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{education_id}",
    response_model=EducationResponse,
)
def get_education(
    education_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EducationService.get_education(
        db=db,
        education_id=education_id,
        current_user=current_user,
    )


@router.put(
    "/{education_id}",
    response_model=EducationResponse,
)
def update_education(
    education_id: int,
    education: EducationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EducationService.update_education(
        db=db,
        education_id=education_id,
        education_data=education,
        current_user=current_user,
    )


@router.delete(
    "/{education_id}",
)
def delete_education(
    education_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return EducationService.delete_education(
        db=db,
        education_id=education_id,
        current_user=current_user,
    )
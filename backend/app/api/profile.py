from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.profile_schemas import (
    ProfileCreate,
    ProfileResponse,
    ProfileUpdate,
)
from app.services.profile_service import ProfileService

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.post(
    "",
    response_model=ProfileResponse,
)
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ProfileService.create_profile(
        db,
        profile,
        current_user,
    )


@router.get(
    "",
    response_model=ProfileResponse,
)
def get_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ProfileService.get_profile(
        db,
        current_user,
    )


@router.put(
    "",
    response_model=ProfileResponse,
)
def update_profile(
    profile: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ProfileService.update_profile(
        db,
        profile,
        current_user,
    )


@router.delete("")
def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return ProfileService.delete_profile(
        db,
        current_user,
    )
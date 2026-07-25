from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.experience_repository import ExperienceRepository
from app.schemas.experience_schemas import (
    ExperienceCreate,
    ExperienceUpdate,
)


class ExperienceService:

    @staticmethod
    def create_experience(
        db: Session,
        experience: ExperienceCreate,
        current_user: User,
    ):
        return ExperienceRepository.create_experience(
            db=db,
            experience=experience,
            user_id=current_user.id,
        )

    @staticmethod
    def get_experiences(
        db: Session,
        current_user: User,
    ):
        return ExperienceRepository.get_experiences_by_user(
            db=db,
            user_id=current_user.id,
        )
    
    @staticmethod
    def get_experience(
        db: Session,
        experience_id: int,
        current_user: User,
    ):
        experience = ExperienceRepository.get_experience_by_id(
            db=db,
            experience_id=experience_id,
            user_id=current_user.id,
        )

        if not experience:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Experience not found",
            )

        return experience

    @staticmethod
    def update_experience(
        db: Session,
        experience_id: int,
        experience_data: ExperienceUpdate,
        current_user: User,
    ):
        experience = ExperienceRepository.get_experience_by_id(
            db=db,
            experience_id=experience_id,
            user_id=current_user.id,
        )

        if not experience:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Experience not found",
            )

        return ExperienceRepository.update_experience(
            db=db,
            db_experience=experience,
            experience=experience_data,
        )

    @staticmethod
    def delete_experience(
        db: Session,
        experience_id: int,
        current_user: User,
    ):
        experience = ExperienceRepository.get_experience_by_id(
            db=db,
            experience_id=experience_id,
            user_id=current_user.id,
        )

        if not experience:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Experience not found",
            )

        ExperienceRepository.delete_experience(
            db=db,
            db_experience=experience,
        )

        return {"message": "Experience deleted successfully"}
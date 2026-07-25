from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.education_repository import EducationRepository
from app.schemas.education_schemas import (
    EducationCreate,
    EducationUpdate,
)


class EducationService:

    @staticmethod
    def create_education(
        db: Session,
        education: EducationCreate,
        current_user: User,
    ):
        return EducationRepository.create_education(
            db=db,
            education=education,
            user_id=current_user.id,
        )

    @staticmethod
    def get_educations(
        db: Session,
        current_user: User,
    ):
        return EducationRepository.get_educations_by_user(
            db=db,
            user_id=current_user.id,
        )

    @staticmethod
    def get_education(
        db: Session,
        education_id: int,
        current_user: User,
    ):
        education = EducationRepository.get_education_by_id(
            db=db,
            education_id=education_id,
            user_id=current_user.id,
        )

        if not education:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Education not found",
            )

        return education

    @staticmethod
    def update_education(
        db: Session,
        education_id: int,
        education_data: EducationUpdate,
        current_user: User,
    ):
        education = EducationRepository.get_education_by_id(
            db=db,
            education_id=education_id,
            user_id=current_user.id,
        )

        if not education:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Education not found",
            )

        return EducationRepository.update_education(
            db=db,
            db_education=education,
            education=education_data,
        )

    @staticmethod
    def delete_education(
        db: Session,
        education_id: int,
        current_user: User,
    ):
        education = EducationRepository.get_education_by_id(
            db=db,
            education_id=education_id,
            user_id=current_user.id,
        )

        if not education:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Education not found",
            )

        EducationRepository.delete_education(
            db=db,
            db_education=education,
        )

        return {"message": "Education deleted successfully"}
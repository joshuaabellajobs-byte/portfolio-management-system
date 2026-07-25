from sqlalchemy.orm import Session

from app.models.education import Education
from app.schemas.education_schemas import (
    EducationCreate,
    EducationUpdate,
)


class EducationRepository:

    @staticmethod
    def create_education(
        db: Session,
        education: EducationCreate,
        user_id: int,
    ) -> Education:
        db_education = Education(
            **education.model_dump(),
            user_id=user_id,
        )

        db.add(db_education)
        db.commit()
        db.refresh(db_education)

        return db_education

    @staticmethod
    def get_educations_by_user(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(Education)
            .filter(Education.user_id == user_id)
            .all()
        )

    @staticmethod
    def get_education_by_id(
        db: Session,
        education_id: int,
        user_id: int,
    ):
        return (
            db.query(Education)
            .filter(
                Education.id == education_id,
                Education.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def update_education(
        db: Session,
        db_education: Education,
        education: EducationUpdate,
    ) -> Education:

        update_data = education.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_education, key, value)

        db.commit()
        db.refresh(db_education)

        return db_education

    @staticmethod
    def delete_education(
        db: Session,
        db_education: Education,
    ):
        db.delete(db_education)
        db.commit()
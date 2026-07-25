from sqlalchemy.orm import Session

from app.models.experience import Experience
from app.schemas.experience_schemas import (
    ExperienceCreate,
    ExperienceUpdate,
)


class ExperienceRepository:

    @staticmethod
    def create_experience(
        db: Session,
        experience: ExperienceCreate,
        user_id: int,
    ) -> Experience:
        db_experience = Experience(
            **experience.model_dump(),
            user_id=user_id,
        )

        db.add(db_experience)
        db.commit()
        db.refresh(db_experience)

        return db_experience

    @staticmethod
    def get_experiences_by_user(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(Experience)
            .filter(Experience.user_id == user_id)
            .all()
        )

    @staticmethod
    def get_experience_by_id(
        db: Session,
        experience_id: int,
        user_id: int,
    ):
        return (
            db.query(Experience)
            .filter(
                Experience.id == experience_id,
                Experience.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def update_experience(
        db: Session,
        db_experience: Experience,
        experience: ExperienceUpdate,
    ) -> Experience:

        update_data = experience.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_experience, key, value)

        db.commit()
        db.refresh(db_experience)

        return db_experience

    @staticmethod
    def delete_experience(
        db: Session,
        db_experience: Experience,
    ):
        db.delete(db_experience)
        db.commit()
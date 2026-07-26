from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile_schemas import ProfileCreate, ProfileUpdate


class ProfileRepository:

    @staticmethod
    def create_profile(
        db: Session,
        profile: ProfileCreate,
        user_id: int,
    ) -> Profile:
        db_profile = Profile(
            **profile.model_dump(),
            user_id=user_id,
        )
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        return db_profile

    @staticmethod
    def get_profile_by_user(
        db: Session,
        user_id: int,
    ) -> Profile | None:
        return (
            db.query(Profile)
            .filter(Profile.user_id == user_id)
            .first()
        )

    @staticmethod
    def update_profile(
        db: Session,
        db_profile: Profile,
        profile: ProfileUpdate,
    ) -> Profile:
        update_data = profile.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_profile, key, value)

        db.commit()
        db.refresh(db_profile)
        return db_profile

    @staticmethod
    def delete_profile(
        db: Session,
        db_profile: Profile,
    ) -> None:
        db.delete(db_profile)
        db.commit()

    @staticmethod
    def update_profile_image(
        db: Session,
        db_profile: Profile,
        image_path: str,
    ) -> Profile:
        db_profile.profile_image = image_path

        db.commit()
        db.refresh(db_profile)

        return db_profile

    @staticmethod
    def update_resume_file(
        db: Session,
        db_profile: Profile,
        resume_path: str,
    ) -> Profile:
        db_profile.resume_file = resume_path

        db.commit()
        db.refresh(db_profile)

        return db_profile
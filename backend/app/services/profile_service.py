from fastapi import HTTPException, status, UploadFile

from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.profile_repository import ProfileRepository
from app.schemas.profile_schemas import ProfileCreate, ProfileUpdate
from app.utils.file_upload import FileUpload


class ProfileService:

    @staticmethod
    def create_profile(
        db: Session,
        profile: ProfileCreate,
        current_user: User,
    ):
        existing = ProfileRepository.get_profile_by_user(
            db,
            current_user.id,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Profile already exists.",
            )

        return ProfileRepository.create_profile(
            db,
            profile,
            current_user.id,
        )

    @staticmethod
    def get_profile(
        db: Session,
        current_user: User,
    ):
        profile = ProfileRepository.get_profile_by_user(
            db,
            current_user.id,
        )

        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found.",
            )

        return profile

    @staticmethod
    def update_profile(
        db: Session,
        profile: ProfileUpdate,
        current_user: User,
    ):
        db_profile = ProfileRepository.get_profile_by_user(
            db,
            current_user.id,
        )

        if not db_profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found.",
            )

        return ProfileRepository.update_profile(
            db,
            db_profile,
            profile,
        )

    @staticmethod
    def delete_profile(
        db: Session,
        current_user: User,
    ):
        db_profile = ProfileRepository.get_profile_by_user(
            db,
            current_user.id,
        )

        if not db_profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found.",
            )

        ProfileRepository.delete_profile(
            db,
            db_profile,
        )

        return {
            "message": "Profile deleted successfully."
        }

    @staticmethod
    def upload_profile_image(
        db: Session,
        file: UploadFile,
        current_user: User,
    ):
        profile = ProfileRepository.get_profile_by_user(
            db,
            current_user.id,
        )

        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found.",
            )

        image_path = FileUpload.save_file(
            file=file,
            folder="uploads/profiles",
            allowed_extensions=[
                ".jpg",
                ".jpeg",
                ".png",
            ],
        )

        return ProfileRepository.update_profile_image(
            db,
            profile,
            image_path,
        )

    @staticmethod
    def upload_resume(
        db: Session,
        file: UploadFile,
        current_user: User,
    ):
        profile = ProfileRepository.get_profile_by_user(
            db,
            current_user.id,
        )

        if not profile:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Profile not found.",
            )

        resume_path = FileUpload.save_file(
            file=file,
            folder="uploads/resumes",
            allowed_extensions=[".pdf"],
        )

        return ProfileRepository.update_resume_file(
            db,
            profile,
            resume_path,
        )
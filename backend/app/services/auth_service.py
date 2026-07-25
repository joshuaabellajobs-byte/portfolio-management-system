from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate
from app.utils.security import hash_password


class AuthService:

    @staticmethod
    def register_user(db: Session, user: UserCreate):

        if UserRepository.get_by_username(db, user.username):
            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        if UserRepository.get_by_email(db, user.email):
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        new_user = User(
            username=user.username,
            email=user.email,
            password_hash=hash_password(user.password)
        )

        return UserRepository.create_user(db, new_user)
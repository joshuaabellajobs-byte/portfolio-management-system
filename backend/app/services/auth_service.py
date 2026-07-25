from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserLogin, Token
from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token,
)


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


    @staticmethod
    def login_user(db: Session, user: UserLogin) -> Token:
        """
        Authenticate a user and return a JWT access token.
        """
        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if not existing_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        if not verify_password(
            user.password,
            existing_user.password_hash
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            data={
                "sub": existing_user.email
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer"
        )
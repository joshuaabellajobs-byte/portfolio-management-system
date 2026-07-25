from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.skill_repository import SkillRepository
from app.schemas.skill_schemas import (
    SkillCreate,
    SkillUpdate,
)


class SkillService:

    @staticmethod
    def create_skill(
        db: Session,
        skill: SkillCreate,
        current_user: User,
    ):
        return SkillRepository.create_skill(
            db=db,
            skill=skill,
            user_id=current_user.id,
        )

    @staticmethod
    def get_skills(
        db: Session,
        current_user: User,
    ):
        return SkillRepository.get_skills_by_user(
            db=db,
            user_id=current_user.id,
        )
    
    @staticmethod
    def get_skill(
        db: Session,
        skill_id: int,
        current_user: User,
    ):
        skill = SkillRepository.get_skill_by_id(
            db=db,
            skill_id=skill_id,
            user_id=current_user.id,
        )

        if not skill:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Skill not found",
            )

        return skill

    @staticmethod
    def update_skill(
        db: Session,
        skill_id: int,
        skill_data: SkillUpdate,
        current_user: User,
    ):
        skill = SkillRepository.get_skill_by_id(
            db=db,
            skill_id=skill_id,
            user_id=current_user.id,
        )

        if not skill:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Skill not found",
            )

        return SkillRepository.update_skill(
            db=db,
            db_skill=skill,
            skill=skill_data,
        )

    @staticmethod
    def delete_skill(
        db: Session,
        skill_id: int,
        current_user: User,
    ):
        skill = SkillRepository.get_skill_by_id(
            db=db,
            skill_id=skill_id,
            user_id=current_user.id,
        )

        if not skill:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Skill not found",
            )

        SkillRepository.delete_skill(
            db=db,
            db_skill=skill,
        )

        return {"message": "Skill deleted successfully"}
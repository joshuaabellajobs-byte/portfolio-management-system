from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.schemas.skill_schemas import SkillCreate, SkillUpdate


class SkillRepository:

    @staticmethod
    def create_skill(db: Session, skill: SkillCreate, user_id: int) -> Skill:
        db_skill = Skill(
            **skill.model_dump(),
            user_id=user_id,
        )

        db.add(db_skill)
        db.commit()
        db.refresh(db_skill)

        return db_skill

    @staticmethod
    def get_skills_by_user(db: Session, user_id: int):
        return (
            db.query(Skill)
            .filter(Skill.user_id == user_id)
            .all()
        )

    @staticmethod
    def get_skill_by_id(db: Session, skill_id: int, user_id: int):
        return (
            db.query(Skill)
            .filter(
                Skill.id == skill_id,
                Skill.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def update_skill(
        db: Session,
        db_skill: Skill,
        skill: SkillUpdate,
    ) -> Skill  :

        update_data = skill.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_skill, key, value)

        db.commit()
        db.refresh(db_skill )

        return db_skill

    @staticmethod
    def delete_skill(db: Session, db_skill: Skill):
        db.delete(db_skill)
        db.commit()
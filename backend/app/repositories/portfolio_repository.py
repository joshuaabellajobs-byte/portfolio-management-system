from sqlalchemy.orm import Session, joinedload

from app.models.user import User


class PortfolioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_public_user(self, username: str):
        return (
            self.db.query(User)
            .options(
                joinedload(User.profile),
                joinedload(User.projects),
                joinedload(User.skills),
                joinedload(User.experiences),
                joinedload(User.educations),
                joinedload(User.certificates),
            )
            .filter(
                User.username == username,
                User.is_public.is_(True),
            )
            .first()
        )
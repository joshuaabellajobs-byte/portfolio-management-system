from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.portfolio_repository import PortfolioRepository
from app.schemas.portfolio_schemas import PortfolioResponse


class PortfolioService:
    def __init__(self, db: Session):
        self.repository = PortfolioRepository(db)

    def get_public_portfolio(self, username: str) -> PortfolioResponse:
        user = self.repository.get_public_user(username)

        if user is None:
            raise HTTPException(
                status_code=404,
                detail="Portfolio not found.",
            )

        return PortfolioResponse(
            profile=user.profile,
            projects=user.projects,
            skills=user.skills,
            experiences=user.experiences,
            educations=user.educations,
            certificates=user.certificates,
        )
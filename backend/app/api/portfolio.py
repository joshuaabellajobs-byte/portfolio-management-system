from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.portfolio_schemas import PortfolioResponse
from app.services.portfolio_service import PortfolioService

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


@router.get(
    "/{username}",
    response_model=PortfolioResponse,
)
def get_public_portfolio(
    username: str,
    db: Session = Depends(get_db),
):
    service = PortfolioService(db)
    return service.get_public_portfolio(username)
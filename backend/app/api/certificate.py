from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.certificate_schemas import (
    CertificateCreate,
    CertificateResponse,
    CertificateUpdate,
)
from app.services.certificate_service import CertificateService


router = APIRouter(
    prefix="/certificates",
    tags=["Certificates"],
)


@router.post(
    "",
    response_model=CertificateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_certificate(
    certificate: CertificateCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return CertificateService.create_certificate(
        db=db,
        certificate=certificate,
        current_user=current_user,
    )


@router.get(
    "",
    response_model=List[CertificateResponse],
)
def get_certificates(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return CertificateService.get_certificates(
        db=db,
        current_user=current_user,
    )


@router.get(
    "/{certificate_id}",
    response_model=CertificateResponse,
)
def get_certificate(
    certificate_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return CertificateService.get_certificate(
        db=db,
        certificate_id=certificate_id,
        current_user=current_user,
    )


@router.put(
    "/{certificate_id}",
    response_model=CertificateResponse,
)
def update_certificate(
    certificate_id: int,
    certificate: CertificateUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return CertificateService.update_certificate(
        db=db,
        certificate_id=certificate_id,
        certificate_data=certificate,
        current_user=current_user,
    )


@router.delete("/{certificate_id}")
def delete_certificate(
    certificate_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return CertificateService.delete_certificate(
        db=db,
        certificate_id=certificate_id,
        current_user=current_user,
    )
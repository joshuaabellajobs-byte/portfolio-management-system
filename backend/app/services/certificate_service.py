from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.certificate_repository import CertificateRepository
from app.schemas.certificate_schemas import (
    CertificateCreate,
    CertificateUpdate,
)


class CertificateService:

    @staticmethod
    def create_certificate(
        db: Session,
        certificate: CertificateCreate,
        current_user: User,
    ):
        return CertificateRepository.create_certificate(
            db=db,
            certificate=certificate,
            user_id=current_user.id,
        )

    @staticmethod
    def get_certificates(
        db: Session,
        current_user: User,
    ):
        return CertificateRepository.get_certificates_by_user(
            db=db,
            user_id=current_user.id,
        )

    @staticmethod
    def get_certificate(
        db: Session,
        certificate_id: int,
        current_user: User,
    ):
        certificate = CertificateRepository.get_certificate_by_id(
            db=db,
            certificate_id=certificate_id,
            user_id=current_user.id,
        )

        if not certificate:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Certificate not found",
            )

        return certificate

    @staticmethod
    def update_certificate(
        db: Session,
        certificate_id: int,
        certificate_data: CertificateUpdate,
        current_user: User,
    ):
        certificate = CertificateRepository.get_certificate_by_id(
            db=db,
            certificate_id=certificate_id,
            user_id=current_user.id,
        )

        if not certificate:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Certificate not found",
            )

        return CertificateRepository.update_certificate(
            db=db,
            db_certificate=certificate,
            certificate=certificate_data,
        )

    @staticmethod
    def delete_certificate(
        db: Session,
        certificate_id: int,
        current_user: User,
    ):
        certificate = CertificateRepository.get_certificate_by_id(
            db=db,
            certificate_id=certificate_id,
            user_id=current_user.id,
        )

        if not certificate:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Certificate not found",
            )

        CertificateRepository.delete_certificate(
            db=db,
            db_certificate=certificate,
        )

        return {"message": "Certificate deleted successfully"}
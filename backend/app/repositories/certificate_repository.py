from sqlalchemy.orm import Session

from app.models.certificate import Certificate
from app.schemas.certificate_schemas import (
    CertificateCreate,
    CertificateUpdate,
)


class CertificateRepository:

    @staticmethod
    def create_certificate(
        db: Session,
        certificate: CertificateCreate,
        user_id: int,
    ) -> Certificate:
        db_certificate = Certificate(
            **certificate.model_dump(),
            user_id=user_id,
        )

        db.add(db_certificate)
        db.commit()
        db.refresh(db_certificate)

        return db_certificate

    @staticmethod
    def get_certificates_by_user(
        db: Session,
        user_id: int,
    ):
        return (
            db.query(Certificate)
            .filter(Certificate.user_id == user_id)
            .all()
        )

    @staticmethod
    def get_certificate_by_id(
        db: Session,
        certificate_id: int,
        user_id: int,
    ):
        return (
            db.query(Certificate)
            .filter(
                Certificate.id == certificate_id,
                Certificate.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def update_certificate(
        db: Session,
        db_certificate: Certificate,
        certificate: CertificateUpdate,
    ) -> Certificate:

        update_data = certificate.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_certificate, key, value)

        db.commit()
        db.refresh(db_certificate)

        return db_certificate

    @staticmethod
    def delete_certificate(
        db: Session,
        db_certificate: Certificate,
    ):
        db.delete(db_certificate)
        db.commit()
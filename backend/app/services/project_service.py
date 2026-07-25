from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.schemas.project_schemas import (
    ProjectCreate,
    ProjectUpdate,
)


class ProjectService:

    @staticmethod
    def create_project(
        db: Session,
        project: ProjectCreate,
        current_user: User,
    ):
        return ProjectRepository.create_project(
            db=db,
            project=project,
            user_id=current_user.id,
        )

    @staticmethod
    def get_projects(
        db: Session,
        current_user: User,
    ):
        return ProjectRepository.get_projects_by_user(
            db=db,
            user_id=current_user.id,
        )

    @staticmethod
    def get_project(
        db: Session,
        project_id: int,
        current_user: User,
    ):
        project = ProjectRepository.get_project_by_id(
            db=db,
            project_id=project_id,
            user_id=current_user.id,
        )

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
            )

        return project

    @staticmethod
    def update_project(
        db: Session,
        project_id: int,
        project_data: ProjectUpdate,
        current_user: User,
    ):
        project = ProjectRepository.get_project_by_id(
            db=db,
            project_id=project_id,
            user_id=current_user.id,
        )

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
            )

        return ProjectRepository.update_project(
            db=db,
            db_project=project,
            project=project_data,
        )

    @staticmethod
    def delete_project(
        db: Session,
        project_id: int,
        current_user: User,
    ):
        project = ProjectRepository.get_project_by_id(
            db=db,
            project_id=project_id,
            user_id=current_user.id,
        )

        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found",
            )

        ProjectRepository.delete_project(
            db=db,
            db_project=project,
        )

        return {"message": "Project deleted successfully"}
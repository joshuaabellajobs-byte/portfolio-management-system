from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project_schemas import ProjectCreate, ProjectUpdate


class ProjectRepository:

    @staticmethod
    def create_project(db: Session, project: ProjectCreate, user_id: int) -> Project:
        db_project = Project(
            **project.model_dump(),
            user_id=user_id,
        )

        db.add(db_project)
        db.commit()
        db.refresh(db_project)

        return db_project

    @staticmethod
    def get_projects_by_user(db: Session, user_id: int):
        return (
            db.query(Project)
            .filter(Project.user_id == user_id)
            .all()
        )

    @staticmethod
    def get_project_by_id(db: Session, project_id: int, user_id: int):
        return (
            db.query(Project)
            .filter(
                Project.id == project_id,
                Project.user_id == user_id,
            )
            .first()
        )

    @staticmethod
    def update_project(
        db: Session,
        db_project: Project,
        project: ProjectUpdate,
    ) -> Project:

        update_data = project.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_project, key, value)

        db.commit()
        db.refresh(db_project)

        return db_project

    @staticmethod
    def delete_project(db: Session, db_project: Project):
        db.delete(db_project)
        db.commit()
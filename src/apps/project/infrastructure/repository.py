from apps.core.database.alchemy import db
from apps.core.database.models import ProjectModel
from apps.project.domain.models import ProjectDomain
from apps.project.domain.exceptions import ProjectNotFoundException


class ProjectRepository:
    @classmethod
    def create(cls, body):
        project = ProjectModel(
            name=body.name,
            description=body.description,
            start_date=body.start_date,
            end_date=body.end_date,
            user_id=body.user_id,
            company_id=body.company_id,
        )
        db.session.add(project)
        db.session.commit()
        return ProjectDomain.from_orm(project)

    @classmethod
    def get_all(cls):
        projects = ProjectModel.query.all()
        return [ProjectDomain.from_orm(project) for project in projects]

    @classmethod
    def filter_by(cls, **kwargs):
        projects = ProjectModel.query.filter_by(**kwargs)
        return [ProjectDomain.from_orm(project) for project in projects]

    @classmethod
    def get_by_id(cls, id):
        project = ProjectModel.query.filter_by(id=id).first()
        if project is None:
            raise ProjectNotFoundException(project_id=id)
        return project

    @classmethod
    def update(cls, body, id):
        project = cls.get_by_id(id=id)
        project.name = body.name
        project.description = body.description
        project.start_date = body.start_date
        project.end_date = body.end_date
        project.user_id = body.user_id
        project.company_id = body.company_id
        db.session.add(project)
        db.session.commit()
        db.session.refresh(project)
        return ProjectDomain.from_orm(project)

    @classmethod
    def delete(cls, id):
        project = cls.get_by_id(id=id)
        db.session.delete(project)
        db.session.commit()

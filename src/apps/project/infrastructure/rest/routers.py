from http import HTTPStatus
from flask_openapi3 import APIBlueprint
from .schemes import (
    ProjectBody,
    ProjectResponse,
    ProjectListResponse,
    ProjectUpdatePath,
    ProjectDeletePath,
    ProjectDaysListResponse,
    ProjectDaysResponse,
)
from apps.project.application.services import (
    ProjectCreateService,
    ProjectListService,
    ProjectUpdateService,
    ProjectDeleteService,
)
from apps.project.infrastructure.repository import ProjectRepository
from apps.user.infrastructure.repository import UserRepository
from apps.company.infrastructure.repository import CompanyRepository
from apps.project.infrastructure.handle_errors import project_not_found
from apps.user.infrastructure.handle_errors import user_not_found
from apps.company.infrastructure.handle_errors import company_not_found

from apps.company.domain.exceptions import CompanyNotFoundException
from apps.user.domain.exceptions import UserNotFoundException
from apps.project.domain.exceptions import ProjectNotFoundException


api = APIBlueprint(
    "project_api",
    __name__,
    url_prefix="/api/projects",
)


@api.get(
    "/",
    responses={"200": ProjectListResponse},
)
def project_list():
    repository = ProjectRepository
    results = ProjectListService.execute(repository)
    response = ProjectListResponse(
        __root__=[ProjectResponse(**result.dict()).dict() for result in results]
    )

    return response.json(), HTTPStatus.OK


@api.get(
    "/days/",
    responses={"200": ProjectDaysListResponse},
)
def project_days_list():
    repository = ProjectRepository
    results = ProjectListService.execute(repository)
    response = ProjectDaysListResponse(
        __root__=[ProjectDaysResponse(**result.dict()).dict() for result in results]
    )

    return response.json(), HTTPStatus.OK


@api.post(
    "/",
    responses={"201": ProjectResponse},
)
def project_create(body: ProjectBody):
    repository = ProjectRepository
    user_repository = UserRepository
    company_repository = CompanyRepository
    result = ProjectCreateService.execute(
        repository, user_repository, company_repository, body
    )
    return ProjectResponse(**result.dict()).json(), HTTPStatus.CREATED


@api.put(
    "/<int:project_id>/",
    responses={"200": ProjectResponse},
)
def project_update(body: ProjectBody, path: ProjectUpdatePath):
    repository = ProjectRepository
    user_repository = UserRepository
    company_repository = CompanyRepository
    project_id = path.project_id
    result = ProjectUpdateService.execute(
        repository, user_repository, company_repository, body, project_id
    )
    return ProjectResponse(**result.dict()).json(), HTTPStatus.OK


@api.delete(
    "/<int:project_id>/",
    responses={},
)
def project_delete(path: ProjectDeletePath):
    repository = ProjectRepository

    project_id = path.project_id
    ProjectDeleteService.execute(repository, project_id)
    return {}, HTTPStatus.NO_CONTENT


api.register_error_handler(ProjectNotFoundException, project_not_found)
api.register_error_handler(CompanyNotFoundException, company_not_found)
api.register_error_handler(UserNotFoundException, user_not_found)

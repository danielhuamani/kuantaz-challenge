from http import HTTPStatus
from flask import jsonify, request
from flask_openapi3 import APIBlueprint
from .schemes import CompanyBody, CompanyResponse, CompanyListResponse, CompanyUpdatePath, CompanyDeletePath
from apps.company.services import CompanyCreateService, CompanyListService, CompanyUpdateService, CompanyDeleteService
from apps.company.repository import CompanyRepository
from apps.company.handle_errors import company_not_found
from apps.company.domain.exceptions import CompanyNotFoundException


api = APIBlueprint(
    "api",
    __name__,
    url_prefix="/api/companies",
)


@api.get(
    "/",
    responses={
        "200": CompanyListResponse
    },
)
def company_list():
    repo = CompanyRepository
    result = CompanyListService.execute(repo)
    response = CompanyListResponse(__root__=[
        CompanyResponse(**company.dict()).dict() for company in result
    ])
    
    return response.json(), HTTPStatus.OK


@api.post(
    "/",
    responses={
        "201": CompanyResponse
    },
)
def company_create(body: CompanyBody):
    repo = CompanyRepository
    result = CompanyCreateService.execute(repo,body)
    
    return CompanyResponse(**result.dict()).json(), HTTPStatus.CREATED


@api.put(
    "/<int:company_id>/",
    responses={
        "200": CompanyResponse
    },
)
def company_update(body: CompanyBody, path: CompanyUpdatePath):
    repo = CompanyRepository
    company_id = path.company_id
    result = CompanyUpdateService.execute(repo, body, company_id)
    return CompanyResponse(**result.dict()).json(), HTTPStatus.OK


@api.delete(
    "/<int:company_id>/",
    responses={
    },
)
def company_delete(path: CompanyDeletePath):
    repo = CompanyRepository
    company_id  = path.company_id
    CompanyDeleteService.execute(repo, company_id)
    return {}, HTTPStatus.OK


api.register_error_handler(
    CompanyNotFoundException, company_not_found
)
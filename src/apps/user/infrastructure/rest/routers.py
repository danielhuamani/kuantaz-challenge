from http import HTTPStatus
from flask import jsonify, request
from flask_openapi3 import APIBlueprint
from .schemes import (
    UserBody,
    UserResponse,
    UserListResponse,
    UserProjectResponse,
    UserUpdatePath,
    UserDeletePath,
    UserFilterQuery,
)
from apps.user.application.services import (
    UserCreateService,
    UserListService,
    UserDetailService,
    UserUpdateService,
    UserDeleteService,
)
from apps.user.infrastructure.repository import UserRepository
from apps.user.infrastructure.handle_errors import user_not_found
from apps.user.domain.exceptions import UserNotFoundException


api = APIBlueprint(
    "user_api",
    __name__,
    url_prefix="/api/users",
)


@api.get(
    "/",
    responses={"200": UserListResponse},
)
def user_list(query: UserFilterQuery):
    repo = UserRepository
    document = query.document
    results = UserListService.execute(repo, document)
    response = UserListResponse(
        __root__=[UserProjectResponse(**result.dict()).dict() for result in results]
    )

    return response.json(), HTTPStatus.OK


@api.get(
    "/<int:user_id>/",
    responses={"200": UserListResponse},
)
def user_detail(path: UserUpdatePath):
    repo = UserRepository
    user_id = path.user_id
    result = UserDetailService.execute(repo, user_id)
    return UserResponse(**result.dict()).json(), HTTPStatus.OK


@api.post(
    "/",
    responses={"201": UserResponse},
)
def user_create(body: UserBody):
    repo = UserRepository
    result = UserCreateService.execute(repo, body)

    return UserResponse(**result.dict()).json(), HTTPStatus.CREATED


@api.put(
    "/<int:user_id>/",
    responses={"200": UserResponse},
)
def user_update(body: UserBody, path: UserUpdatePath):
    repo = UserRepository
    user_id = path.user_id
    result = UserUpdateService.execute(repo, body, user_id)
    return UserResponse(**result.dict()).json(), HTTPStatus.OK


@api.delete(
    "/<int:user_id>/",
    responses={},
)
def user_delete(path: UserDeletePath):
    repo = UserRepository
    user_id = path.user_id
    UserDeleteService.execute(repo, user_id)
    return {}, HTTPStatus.NO_CONTENT


api.register_error_handler(UserNotFoundException, user_not_found)

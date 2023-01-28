from http import HTTPStatus

from flask import jsonify

from apps.user.domain.exceptions import UserNotFoundException
from apps.core.infrastructure.schemes import Error404NotFoundObject


def user_not_found(e: UserNotFoundException):
    error = Error404NotFoundObject(code=e.code, description=e.message)
    return jsonify(error.dict()), HTTPStatus.NOT_FOUND

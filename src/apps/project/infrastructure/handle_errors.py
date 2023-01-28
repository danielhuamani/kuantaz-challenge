from http import HTTPStatus

from flask import jsonify

from apps.project.domain.exceptions import ProjectNotFoundException
from apps.core.infrastructure.schemes import Error404NotFoundObject


def project_not_found(e: ProjectNotFoundException):
    error = Error404NotFoundObject(code=e.code, description=e.message)
    return jsonify(error.dict()), HTTPStatus.NOT_FOUND

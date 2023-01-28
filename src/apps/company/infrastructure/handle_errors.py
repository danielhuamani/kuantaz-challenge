from http import HTTPStatus

from flask import jsonify

from apps.company.domain.exceptions import CompanyNotFoundException
from apps.core.infrastructure.schemes import Error404NotFoundObject


def company_not_found(e: CompanyNotFoundException):
    error = Error404NotFoundObject(code=e.code, description=e.message)
    return jsonify(error.dict()), HTTPStatus.NOT_FOUND

from http import HTTPStatus
from flask_openapi3 import APIBlueprint


api = APIBlueprint(
    "api",
    __name__,
    url_prefix="/api",
)

@api.get(
    "/hello",
    responses={},
)
def hello():
   
    return {}, HTTPStatus.OK

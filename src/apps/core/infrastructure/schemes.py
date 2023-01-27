from pydantic import BaseModel


class Error404NotFoundObject(BaseModel):
    code: str = "Not_found"
    description: str = "Object not found"

from typing import List, Optional
from datetime import date
from pydantic import BaseModel
from apps.project.infrastructure.rest.schemes import ProjectResponse


class UserBody(BaseModel):

    name : str
    last_name : str
    document : str
    birth_date : date
    occupation : str
    age : int


class UserResponse(BaseModel):
    id : int
    name : str
    last_name : str
    document : str
    birth_date : date
    occupation : str
    age : int


class UserProjectResponse(BaseModel):
    id : int
    name : str
    last_name : str
    document : str
    birth_date : date
    occupation : str
    age : int
    projects: List[ProjectResponse] = []

class UserListResponse(BaseModel):
    __root__ : List[UserProjectResponse]


class UserUpdatePath(BaseModel):
    user_id : int


class UserDeletePath(UserUpdatePath):
    ...


class UserFilterQuery(BaseModel):
    document : Optional[str]
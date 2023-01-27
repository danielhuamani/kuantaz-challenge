from typing import List, Optional
from datetime import date
from pydantic import BaseModel, validator


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


class UserListResponse(BaseModel):
    __root__ : List[UserResponse]


class UserUpdatePath(BaseModel):
    user_id : int


class UserDeletePath(UserUpdatePath):
    ...


class UserFilterQuery(BaseModel):
    document : Optional[str]
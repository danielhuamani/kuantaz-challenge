from typing import List
from datetime import datetime
from pydantic import BaseModel, validator


class CompanyBody(BaseModel):

    name : str
    description : str
    address : str


class CompanyResponse(BaseModel):
    id : int
    created_at : datetime
    name : str
    description : str
    address : str


class CompanyListResponse(BaseModel):
    __root__ : List[CompanyResponse]


class CompanyUpdatePath(BaseModel):
    company_id : int


class CompanyDeletePath(CompanyUpdatePath):
    ...
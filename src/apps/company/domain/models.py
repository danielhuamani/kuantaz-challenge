from typing import List
from datetime import datetime, date
from pydantic import BaseModel


class CompanyDomain(BaseModel):
    id: int
    created_at: datetime
    name: str
    description: str
    address: str

    class Config:
        orm_mode = True


class CompanyProjectUserDomain(BaseModel):
    id: int
    name: str
    last_name: str
    document: str
    birth_date: date
    occupation: str
    age: int

    class Config:
        orm_mode = True


class CompanyProjectDomain(BaseModel):
    id: int
    name: str
    description: str
    start_date: date
    end_date: date
    user: CompanyProjectUserDomain

    class Config:
        orm_mode = True


class CompanyWithProjectAndUserDomain(BaseModel):
    id: int
    created_at: datetime
    name: str
    description: str
    address: str
    projects: List[CompanyProjectDomain] = []

    class Config:
        orm_mode = True

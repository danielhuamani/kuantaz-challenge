from typing import List
from datetime import date
from apps.project.domain.models import ProjectDomain
from pydantic import BaseModel


class UserDomain(BaseModel):
    id: int
    name: str
    last_name: str
    document: str
    birth_date: date
    occupation: str
    age: int
    projects: List[ProjectDomain] = []

    class Config:
        orm_mode = True

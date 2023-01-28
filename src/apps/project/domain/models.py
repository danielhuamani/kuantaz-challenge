from datetime import date
from pydantic import BaseModel


class ProjectDomain(BaseModel):
    id: int
    name: str
    description: str
    start_date: date
    end_date: date
    user_id: int
    company_id: int

    class Config:
        orm_mode = True

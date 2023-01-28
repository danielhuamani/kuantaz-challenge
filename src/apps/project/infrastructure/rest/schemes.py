from typing import List, Optional
from datetime import date
from pydantic import BaseModel, validator


class ProjectBody(BaseModel):

    name : str
    description : str
    start_date : date
    end_date : date
    user_id : int
    company_id : int

    @validator("end_date")
    def validate_end_date(cls, v, values, **kwargs):
        start_date = values["start_date"]
        if v >= start_date:
            return v
        raise ValueError("end date must be greater than start date")

class ProjectResponse(BaseModel):

    id : int
    name : str
    description : str
    start_date : date
    end_date : date
    user_id : int
    company_id : int


class ProjectListResponse(BaseModel):
    __root__ : List[ProjectResponse]


class ProjectDaysResponse(BaseModel):

    name : str
    end_date : date
    days : Optional[int]

    class Config:
        exclude = {"end_date"}

    @validator("days", pre=True)
    def parse_days(cls, v, values, **kwargs):
        end_date = values["end_date"]
        now = date.today()
        if end_date > now:
            return (end_date - now).days
        return 0


class ProjectDaysListResponse(BaseModel):
    __root__ : List[ProjectDaysResponse]



class ProjectUpdatePath(BaseModel):
    project_id : int


class ProjectDeletePath(ProjectUpdatePath):
    ...

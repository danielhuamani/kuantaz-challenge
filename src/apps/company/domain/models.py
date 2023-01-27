from datetime import datetime
from pydantic import BaseModel


class CompanyDomain(BaseModel):
    id : int
    created_at : datetime
    name : str
    description : str
    address : str

    class Config:
        orm_mode = True
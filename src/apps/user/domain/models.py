from datetime import datetime, date
from pydantic import BaseModel


class UserDomain(BaseModel):
    id : int
    name : str
    last_name : str
    document : str
    birth_date : date
    occupation : str
    age : int

    class Config:
        orm_mode = True


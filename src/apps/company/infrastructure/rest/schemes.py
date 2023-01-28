from typing import List, Optional
from datetime import datetime, date
from pydantic import BaseModel, validator
from apps.company.infrastructure.constants import GOOGLE_MAPS_URL


class CompanyBody(BaseModel):

    name: str
    description: str
    address: str


class CompanyGoogleAddressResponse(BaseModel):
    id: int
    created_at: datetime
    name: str
    description: str
    address: str
    google_address: Optional[str]

    @validator("google_address", pre=True)
    def parse_google_address(cls, v, values, **kwargs):
        print(values, "values")
        return f"{GOOGLE_MAPS_URL}{values['address']}"

    @validator("name", pre=True)
    def parse_name(cls, v, values, **kwargs):
        return v[:3]


class CompanyResponse(BaseModel):
    id: int
    created_at: datetime
    name: str
    description: str
    address: str


class CompanyListResponse(BaseModel):
    __root__: List[CompanyResponse]


class CompanyListGoogleAddressResponse(BaseModel):
    __root__: List[CompanyGoogleAddressResponse]


class CompanyUpdatePath(BaseModel):
    company_id: int


class CompanyDeletePath(CompanyUpdatePath):
    ...


class CompanyDetailPath(CompanyUpdatePath):
    ...


class CompanyProjectUserNestedDomain(BaseModel):
    id: int
    name: str
    last_name: str
    document: str
    birth_date: date
    occupation: str
    age: int

    class Config:
        orm_mode = True


class CompanyProjectNestedResponse(BaseModel):
    id: int
    name: str
    description: str
    start_date: date
    end_date: date
    user: CompanyProjectUserNestedDomain

    class Config:
        orm_mode = True


class CompanyNestedResponse(BaseModel):
    id: int
    created_at: datetime
    name: str
    description: str
    address: str
    projects: List[CompanyProjectNestedResponse]


class CompanyNestedListResponse(BaseModel):
    __root__: List[CompanyNestedResponse]

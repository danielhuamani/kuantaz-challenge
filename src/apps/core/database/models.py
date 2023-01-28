from __future__ import annotations

from datetime import datetime
import enum
import json
from typing import List



from .alchemy import BaseModel, db


class CompanyModel(BaseModel):
    __tablename__ = "company"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String)
    description = db.Column(db.String)
    address = db.Column(db.String)

    projects = db.relationship("ProjectModel", back_populates="company")

    def __init__(self, name, description, address):
        self.name = name
        self.description = description
        self.address = address
        

    def __repr__(self):
        return f"<company name: {self.name}"

class ProjectModel(BaseModel):
    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("UserModel", back_populates="projects")
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    company = db.relationship("CompanyModel", back_populates="projects")

    def __repr__(self):
        return f"<project name: {self.name}"

class UserModel(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    document = db.Column(db.String)
    birth_date = db.Column(db.DateTime)
    occupation = db.Column(db.String)
    age = db.Column(db.Integer)

    projects = db.relationship("ProjectModel", back_populates="user")

    def __repr__(self):
        return f"<user name: {self.name}"
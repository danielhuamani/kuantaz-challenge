from apps.core.database.alchemy import db
from apps.core.database.models import CompanyModel
from apps.company.domain.models import CompanyDomain
from apps.company.domain.exceptions import CompanyNotFoundException

class CompanyRepository:

    @classmethod
    def create(cls, body):
        company = CompanyModel(
            name=body.name,
            address=body.address,
            description=body.description
        )
        db.session.add(company)
        db.session.commit()
        return CompanyDomain.from_orm(company)
    
    @classmethod
    def get_all(cls):
        companies = CompanyModel.query.all()
        return [CompanyDomain.from_orm(company) for company in companies]

    @classmethod
    def get_by_id(cls, id):
        company = CompanyModel.query.filter_by(id=id).first()
        if company is None:
            raise CompanyNotFoundException(company_id=id)
        return company
    
    @classmethod
    def update(cls, body, id):
        company = cls.get_by_id(id=id)
        company.address = body.address
        company.name = body.name
        company.description = body.description
        db.session.add(company)
        db.session.commit()
        db.session.refresh(company)
        return CompanyDomain.from_orm(company)
    
    @classmethod
    def delete(cls, id):
        company = cls.get_by_id(id=id)
        db.session.delete(company)
        db.session.commit()

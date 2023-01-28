class CompanyCreateService:

    @classmethod
    def execute(self, repository, body):
        company_domain = repository.create(body)
        return company_domain


class CompanyListService:

    @classmethod
    def execute(self, repository):
        companies = repository.get_all()
        return companies


class CompanyUpdateService:

    @classmethod
    def execute(self, repository, body, company_id):
        company = repository.update(body, company_id)
        return company


class CompanyDeleteService:

    @classmethod
    def execute(self, repository, company_id):
        repository.delete(company_id)
        return company_id


class CompanyDetailService:

    @classmethod
    def execute(self, repository, company_id):
        company = repository.get_all_nested(id=company_id)
        return company
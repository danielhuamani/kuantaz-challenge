from typing import Optional


class CompanyNotFoundException(Exception):
    code: str = "COMPANY_NOT_FOUND"
    message: str = "Company not found"
    company_id: Optional[int] = None

    def __init__(self, message: Optional[str] = None, company_id: Optional[int] = None):
        if message:
            self.message = message
        self.company_id = company_id
        super().__init__(self.message)

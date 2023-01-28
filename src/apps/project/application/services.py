class ProjectCreateService:
    @classmethod
    def execute(self, repository, user_repository, company_repository, body):
        user_repository.get_instance(body.user_id)
        company_repository.get_by_id(body.company_id)
        project = repository.create(body)
        return project


class ProjectListService:
    @classmethod
    def execute(self, repository):
        projects = repository.get_all()
        return projects


class ProjectUpdateService:
    @classmethod
    def execute(
        self, repository, user_repository, company_repository, body, project_id
    ):
        user_repository.get_instance(body.user_id)
        company_repository.get_by_id(body.company_id)
        project = repository.update(body, project_id)
        return project


class ProjectDeleteService:
    @classmethod
    def execute(self, repository, project_id):
        repository.delete(project_id)
        return project_id

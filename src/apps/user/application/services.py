class UserCreateService:

    @classmethod
    def execute(self, repository, body):
        user = repository.create(body)
        return user


class UserListService:

    @classmethod
    def execute(self, repository, document):
        if document:
            users = repository.filter_by(document=document)
        else:
            users = repository.get_all()
        return users


class UserDetailService:

    @classmethod
    def execute(self, repository, user_id):
        user = repository.get_instance(user_id)
        return user

class UserUpdateService:

    @classmethod
    def execute(self, repository, body, user_id):
        user = repository.update(body, user_id)
        return user


class UserDeleteService:

    @classmethod
    def execute(self, repository, user_id):
        repository.delete(user_id)
        return user_id

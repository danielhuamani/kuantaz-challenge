from apps.core.database.alchemy import db
from apps.core.database.models import UserModel
from apps.user.domain.models import UserDomain
from apps.user.domain.exceptions import UserNotFoundException

class UserRepository:

    @classmethod
    def create(cls, body):
        user = UserModel(
            name = body.name,
            last_name = body.last_name,
            document = body.document,
            birth_date = body.birth_date,
            occupation = body.occupation,
            age = body.age
        )
        db.session.add(user)
        db.session.commit()
        return UserDomain.from_orm(user)
    
    @classmethod
    def get_all(cls):
        users = UserModel.query.all()
        return [UserDomain.from_orm(user) for user in users]

    @classmethod
    def filter_by(cls, **kwargs):
        users = UserModel.query.filter_by(**kwargs)
        return [UserDomain.from_orm(user) for user in users]


    @classmethod
    def _get_by_id(cls, id):
        user = UserModel.query.filter_by(id=id).first()
        if user is None:
            raise UserNotFoundException(user_id=id)
        return user
    
    @classmethod
    def get_instance(cls, id):
        user = cls._get_by_id(id=id)
        return UserDomain.from_orm(user)
    

    @classmethod
    def update(cls, body, id):
        user = cls._get_by_id(id=id)
        user.name = body.name
        user.last_name = body.last_name
        user.document = body.document
        user.birth_date = body.birth_date
        user.occupation = body.occupation
        user.age = body.age
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        return UserDomain.from_orm(user)

    @classmethod
    def delete(cls, id):
        user = cls._get_by_id(id=id)
        db.session.delete(user)
        db.session.commit()

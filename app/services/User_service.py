import inject
import typing
from app.models.user_model import User
from app.repositories.user_repository import UserRepository
class UserService:
    user_repository=inject.attr(UserRepository)

    def getUser(self,id)->User:
        user=self.user_repository.getUser(id=id)
        return user


    def getAll(self)->typing.List[User]:
        list = self.user_repository.getAll()
        return list

    def getPassword(self,id)->User.password:
        password=self.user_repository.getPassword(id=id)
        return password

    def getEmail(self,id)->User.email:
        email=self.user_repository.getEmail(id=id)
        return email

    def getRoleID(self,id)->User.role_id:
        role_id=self.user_repository.getRoleID(id=id)
        return role_id
from repositories.user_repository import UserRepository
from src.user import User

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user: User) -> None:
        self.user_repo.save(user)

    def get_all_users(self):
        return self.user_repo.find_all()

    def get_user_by_id(self, user_id: str) -> User:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return user

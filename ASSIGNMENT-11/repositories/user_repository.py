from .repository import Repository
from src.user import User

class UserRepository(Repository[User, str]):
    """User Repository extends the generic Repository for User objects."""
    pass

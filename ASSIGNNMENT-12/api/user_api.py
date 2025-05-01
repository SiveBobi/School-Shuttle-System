from fastapi import APIRouter, HTTPException
from services.user_service import UserService
from repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from src.user import User

router = APIRouter(prefix="/api/users", tags=["Users"])

user_service = UserService(InMemoryUserRepository())

@router.get("/")
def get_all_users():
    return user_service.get_all_users()

@router.post("/")
def create_user(user: User):
    user_service.create_user(user)
    return {"message": "User created successfully"}

@router.get("/{user_id}")
def get_user_by_id(user_id: str):
    try:
        return user_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

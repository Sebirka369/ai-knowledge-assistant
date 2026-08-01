from fastapi import APIRouter, Depends

from app.schemas.user import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.dependencies.services import get_auth_service

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register", response_model=UserResponse)
def register(
    user_data: UserCreate,
    auth_service: AuthService = Depends(get_auth_service),
):
    return auth_service.register_user(user_data)

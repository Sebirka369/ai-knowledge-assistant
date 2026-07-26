from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService


def get_user_repository(
    db: Session,
) -> UserRepository:
    return UserRepository(db)


def get_auth_service(
    repository: UserRepository,
) -> AuthService:
    return AuthService(repository)
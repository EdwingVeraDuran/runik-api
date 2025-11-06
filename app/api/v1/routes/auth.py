from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from datetime import timedelta
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut, UserToken
from app.core.database import get_db
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.config import settings
from jose import JWTError, jwt

from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Authentication"])


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(session=db)


# --- Register ---
@router.post("/register", response_model=UserOut)
def register_user(
    user_in: UserCreate, service: UserService = Depends(get_user_service)
):
    response = service.register_user(
        username=user_in.username, email=user_in.email, password=user_in.password
    )

    if response is HTTPException:
        raise response

    return response


# --- Login ---
@router.post("/login", response_model=UserToken)
async def login(
    user_in: UserLogin, service: UserService = Depends(get_user_service)
): ...

from datetime import timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt

from app.core.config import settings
from app.core.database import get_db
from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class UserService:
    def __init__(self, session: Session):
        self._db = session

    def register_user(
        self, username: str, email: str, password: str
    ) -> User | HTTPException:
        email_result = self._db.execute(select(User).where(User.email == email))
        username_result = self._db.execute(
            select(User).where(User.username == username)
        )
        existing_email = email_result.scalar_one_or_none()
        existing_username = username_result.scalar_one_or_none()

        if existing_email or existing_username:
            return HTTPException(
                status_code=400, detail="Email or username is already registered."
            )

        hashed_pw = get_password_hash(password)
        new_user = User(username=username, email=email, hashed_password=hashed_pw)
        self._db.add(new_user)
        try:
            self._db.commit()
        except IntegrityError:
            self._db.rollback()
            return HTTPException(
                status_code=400, detail="Email or username already registered."
            )
        self._db.refresh(new_user)
        return new_user

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
            )
            email: str = payload.get("sub")
            if not isinstance(email, str) or not email:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        result = await self._db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if user is None:
            raise credentials_exception
        return user

    async def login(self, email: str, password: str) -> dict | HTTPException:
        result = await self._db.execute(select(User).where(User.email == email))
        user = result.scalar_one_or_none()
        if not user or not verify_password(password, user.hashed_password):
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials"
            )

        acces_token_expire = timedelta(minutes=settings.ACCES_TOKEN_EXPIRE_MINUTES)
        token = create_access_token(
            data={"sub": user.email}, expires_delta=acces_token_expire
        )

        return {"access_token": token, "token_type": "bearer"}

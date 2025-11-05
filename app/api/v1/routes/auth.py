from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import timedelta
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserOut, UserToken
from app.core.database import get_db
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])

# --- Register ---
@router.post("/register", response_model=UserOut)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    email_result = await db.execute(select(User).where(User.email == user_in.email))
    username_result = await db.execute(select(User).where(User.username == user_in.username))
    existing_email = email_result.scalar_one_or_none()
    exising_username = username_result.scalar_one_or_none()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email is already registered.")
    if exising_username:
        raise HTTPException(status_code=400, detail="Username is already registeres")
    
    hashed_pw = get_password_hash(user_in.password)
    new_user = User(username=user_in.username, email=user_in.email, hashed_password=hashed_pw)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# --- Login ---
@router.post("/login", response_model=UserToken)
async def login(user_in: UserLogin, db:AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_in.email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
    
    acces_token_expire = timedelta(minutes=settings.ACCES_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(data={"sub": user.email}, expires_delta=acces_token_expire)
    
    return {"access_token": token, "token_type": "bearer"}

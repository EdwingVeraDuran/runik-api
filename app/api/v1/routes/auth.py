from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import timedelta
from app.models.user import User
from app.schemas.user import UserCreate, UserOut
from app.core.database import get_db
from app.core.security import get_password_hash, verify_password, create_acces_token
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])

# --- Register ---
@router.post("/register", response_model=UserOut)
async def register_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user_in.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email is already registered.")
    
    hashed_pw = get_password_hash(user_in.password)
    new_user = User(username=user_in.username, email=user_in.email, hashed_password=hashed_pw)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# --- Login ---
@router.post("/login")
async def login(email: str, password: str, db:AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Icorrect credentials")
    
    acces_token_expire = timedelta(minutes=settings.ACCES_TOKEN_EXPIRE_MINUTES)
    token = create_acces_token(data={"sub": user.email}, expires_delta=acces_token_expire)
    
    return {"acces_token": token, "token_type": "bearer"}
    
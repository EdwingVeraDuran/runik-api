from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    
class UserCreate(UserBase):
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class UserOut(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    
    class Config:
        orm_mode = True

class UserToken(BaseModel):
    access_token: str
    token_type: str
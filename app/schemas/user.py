from pydantic import BaseModel, ConfigDict, EmailStr

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
    model_config = ConfigDict(from_attributes=True)

class UserToken(BaseModel):
    access_token: str
    token_type: str
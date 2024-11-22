from pydantic import BaseModel, EmailStr
from beanie import Document


class User(Document):
    email: EmailStr
    password: str
    
    class Settings:
        name = 'users'


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    
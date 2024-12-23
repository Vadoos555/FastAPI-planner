from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.users import User, TokenResponse
from database.connection import DataBase
from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token


user_router = APIRouter(tags=["User"],)

user_db = DataBase(User)
hash_password = HashPassword()


@user_router.post('/signup')
async def register_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User with this username exists already'
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_db.save(user)
    return {'message': 'User created successfully.'}


@user_router.post('/login', response_model=TokenResponse)
async def login_user(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exit = await User.find_one(User.email == user.username)
    if not user_exit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User does not exist.'
        )
    if hash_password.verify_hash(user.password, user_exit.password):
        access_token = create_access_token(user_exit.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid details passed."
        )

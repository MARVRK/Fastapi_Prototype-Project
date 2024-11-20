from datetime import timedelta, datetime
from typing import Union

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import jwt
from jose.exceptions import JWTError

from app.core.config import setting, Settings

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY, algorithms=Settings.ALGORITHM)
        return payload
    except JWTError as e:
        raise Exception("Token Excpired")


def get_password_hash(password: str) -> str:
   return bcrypt_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)-> bool:
    return bcrypt_context.verify(plain_password,hashed_password)

def create_access_token(data: dict, expires_delta: Union[timedelta,None] = None)-> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithms=setting.ALGORITHM)
    return encode_jwt
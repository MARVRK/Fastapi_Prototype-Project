from typing import Union

from psycopg2 import IntegrityError

from app.db.session import get_db
from app.models.users import User
from sqlalchemy.orm import Session
from app.core.security import get_password_hash, verify_password

from app.schemas.users import UserCreate, UserInDb


def create_user(db: Session, user_create: UserCreate) -> User:
    new_user = User(username=user_create.user_name,
                    email=user_create.email,
                    hashed_password=get_password_hash(user_create.password),
                    role=user_create.role)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "user_name": new_user.username,
        "password": new_user.hashed_password,
        "email": new_user.email,
        "role": new_user.role,}

def get_user(db: Session, username: str) -> Union[User, None]:
    return db.query(User).filter(User.username == username).first()


def auth_user(db: Session, username: str, password: str) -> Union[UserInDb, None]:
    user = get_user(db, username)
    if user and verify_password(password, user.hashed_password):
        return UserInDb(**user.__dict__)
    return None

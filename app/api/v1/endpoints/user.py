from crypt import methods

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.config import Settings
from app.db.session import get_db
from app.schemas.users import UserCreate
from app.services.db_service import create_user

router = APIRouter()


@router.post("/users/", response_model=UserCreate)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db,user)
    if db_user is None:
        raise HTTPException(status_code=409, detail="User already exists")
    return db_user
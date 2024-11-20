from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import setting

engine = create_engine(setting.PATH_DB)
Session_Local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close

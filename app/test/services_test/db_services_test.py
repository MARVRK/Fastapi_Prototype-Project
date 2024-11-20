import pytest
from app.db.session import engine, Session_Local
from sqlalchemy.ext.declarative import declarative_base

from app.schemas.users import UserCreate
from app.services.db_service import create_user


@pytest.fixture(scope="module")
def db_session():
    base = declarative_base()
    base.metadata.create_all(bind=engine)
    db = Session_Local()
    yield db
    db.close()
    base.metadata.drop_all(bind=engine)


@pytest.fixture
def test_user():
    user = UserCreate(
        user_name="test_user",
        password="test_password",
        email="test@example.com",
        role="user"
    )
    return user


def test_create_user(db_session, test_user):
    user = create_user(db_session, test_user)
    assert user.username == test_user.user_name
    assert user.hashed_password == test_user.password
    assert user.email == test_user.email
    assert user.role == test_user.role

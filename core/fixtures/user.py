import pytest
from core.user.models import User

user_data = {
    "username":"test",
    "email":"test@mail.com",
    "password":"test123",
    "firstName":"test",
    "lastName":"test",
}

@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**user_data) 
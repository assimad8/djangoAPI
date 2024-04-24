import pytest
from core.user.models import User

# Create your tests here.

user_data = {
    "username":"test",
    "email":"test@mail.com",
    "firstName":"test",
    "lastName":"test",
    "password":"test123",
}
superuser_data = {
    "username":"testsuper",
    "email":"testsuper@mail.com",
    "firstName":"testsuer",
    "lastName":"testsuper",
    "password":"test123",
}

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**user_data)
    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.firstName == user_data["firstName"]
    assert user.lastName == user_data["lastName"]
@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser(**superuser_data)
    assert user.username == superuser_data["username"]
    assert user.email == superuser_data["email"]
    assert user.firstName == superuser_data["firstName"]
    assert user.lastName == superuser_data["lastName"]
    assert user.is_superuser == True
    assert user.is_staff == True
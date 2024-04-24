import pytest
from rest_framework import status
from core.fixtures import user,client

class TestAuthenticationViewSet:
    endpoint = 'http://127.0.0.1:8000/api/'

    def test_login(self,user,client):
        data = {
            "email":user.email,
            "password":"test123",
        }
        response = client.post(f"{self.endpoint}login/",data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
        assert response.data['user']['id'] == user.public_id.hex       
        assert response.data['user']['username'] == user.username
        assert response.data['user']['email'] == user.email

    @pytest.mark.django_db
    def test_register(self,client):
        data = {
            "username":"testuser",
            "email":"testuser@mail.com",
            "password":"test123",
            "password2":"test123",
            "firstName":"tset",
            "lastName":"tset"
        }
        response = client.post(f"{self.endpoint}register/",data)
        assert response.status_code == status.HTTP_201_CREATED
    def test_refresh(self,client,user):
        data = {
            "email":user.email,
            "password":"test123",
        }
        response = client.post(f"{self.endpoint}login/",data)
        assert response.status_code == status.HTTP_200_OK

        data_refresh = {
            "refresh":  response.data['refresh']
            }
        response = client.post(f"{self.endpoint}refresh/",data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']

from rest_framework import status

from core.fixtures import client,post,user

class TestUserViewSet:
    endpoint = "http://localhost:8000/api/user/"

    def  test_list(self,client,user):
        client.force_authenticate(user=user)

        response = client.get(f"{self.endpoint}")
        assert response.status_code == status.HTTP_200_OK

    def  test_retrieve(self,client,user):
        client.force_authenticate(user=user)

        response = client.get(f"{self.endpoint}{user.public_id}/")
        assert response.status_code == status.HTTP_200_OK

    def test_create(self,client):
        user_data = {
            "username":"testuser",
            "email":"testuser@mail.com",
            "firstName":"testuser",
            "lastName":"testuser",
            "password":"test123"
        }
        response = client.post(f"{self.endpoint}",user_data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update(self,client,user):
        client.force_authenticate(user=user)
        response = client.patch(f"{self.endpoint}{user.public_id}/")

        assert response.status_code == status.HTTP_200_OK




from rest_framework import status
from core.fixtures import user,post,client

class TestPostViewSet:
    endpoint = "http://127.0.0.1:8000/api/post/"

    def test_list(self,client,user,post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_list_anonymous(self,client,post):
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_retrieve(self,client,post,user):
        client.force_authenticate(user=user)
        response = client.get(f"{self.endpoint}{post.public_id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == post.public_id.hex
        assert response.data['body'] == post.body       
        assert response.data['author']['id'] ==         post.author.public_id.hex

    def test_retrieve_anonymous(self,client,post,user):
        response = client.get(f"{self.endpoint}{post.public_id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == post.public_id.hex
        assert response.data['body'] == post.body       
        assert response.data['author']['id'] ==         post.author.public_id.hex

    def test_create(self,user,client):
        client.force_authenticate(user=user)
        data = {
            "author":user.public_id.hex,
            "body":"test post"
        }
        response = client.post(self.endpoint,data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["body"] == data["body"]
        assert response.data["author"]["id"] == data["author"]
    def test_create(self,client):
        data = {
            "author":"test_user",
            "body":"test post"
        }
        response = client.post(self.endpoint,data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update(self,client,post,user):
        client.force_authenticate(user=user)
        data = {
            "author":user.public_id.hex, 
            "body":"updated post"  
        }
        response = client.put(f"{self.endpoint}{post.public_id.hex}/",data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['body'] == data['body']

    def test_update_anonymous(self,client,post):
        data = {
            "author":"test_user", 
            "body":"updated post"  
        }
        response = client.put(f"{self.endpoint}{post.public_id.hex}/",data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete(self,client,user,post):
        client.force_authenticate(user=user)
        response = client.delete(f"{self.endpoint}{post.public_id.hex}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
    def test_delete(self,client,post):
        response = client.delete(f"{self.endpoint}{post.public_id.hex}/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


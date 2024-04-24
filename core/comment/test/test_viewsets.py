from rest_framework import status
from core.fixtures import client,user, post, comment

class TestCommentViewSet:
    endpoint = "http://127.0.0.1:8000/api/post/"

    def test_list(self,post,user,client):
        client.force_authenticate(user=user)
        response = client.get(f"{self.endpoint}{post.public_id}/comment/")
        assert response.status_code == status.HTTP_200_OK

    def test_list_anonymous(self,post,client):
        response = client.get(f"{self.endpoint}{post.public_id}/comment/")
        assert response.status_code == status.HTTP_200_OK

    def test_retrieve(self,post,client,comment,user):
        client.force_authenticate(user=user)
        response = client.get(f"{self.endpoint}{post.public_id}/comment/{comment.public_id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == comment.public_id.hex
        assert response.data['body'] == comment.body
        assert response.data['author'].hex == comment.author.public_id.hex
        assert response.data['id'] == comment.public_id.hex

    def test_retrieve_anonymous(self,post,client,comment):
        response = client.get(f"{self.endpoint}{post.public_id}/comment/{comment.public_id}/")
        assert response.status_code == status.HTTP_200_OK

    def test_create(self,client,post,user):
        client.force_authenticate(user=user)
        comment_data = {
            "author":user.public_id.hex,
            "post":post.public_id.hex,
            "body":"test comment",
        }
        response = client.post(f"{self.endpoint}{post.public_id}/comment/",comment_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['author'].hex == user.public_id.hex
        assert response.data['author'].hex == user.public_id.hex
    
    def test_create_anonymous(self,client,post):
        comment_data = {}
        response = client.post(f"{self.endpoint}{post.public_id}/comment/",comment_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_updated(self,client,user,post,comment):
        client.force_authenticate(user=user)
        comment_data = {
            "author":user.public_id.hex,
            "post":post.public_id.hex,
            "body":"test comment updated",
        }
        response = client.put(f"{self.endpoint}{post.public_id}/comment/{comment.public_id}/",comment_data)
        assert response.status_code == status.HTTP_200_OK

    def test_update_anonymous(self,client,post,comment):
        comment_data = {}
        response = client.put(f"{self.endpoint}{post.public_id}/comment/{comment.public_id}/",comment_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete(self,client,user,post,comment):
        client.force_authenticate(user=user)
        response = client.delete(f"{self.endpoint}{post.public_id}/comment/{comment.public_id}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_anonymous(self,client,post,comment):
        response = client.delete(f"{self.endpoint}{post.public_id}/comment/{comment.public_id}/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        
        
    


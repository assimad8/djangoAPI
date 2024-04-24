import pytest
from core.post.models import Post
from core.fixtures import user


# Create your tests here.
@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user,body="test post")
    assert post.author == user
    assert post.body == "test post"
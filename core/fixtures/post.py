import pytest
from core.fixtures import user
from core.post.models import Post

data_post = {
    "author":user,
    "body":"test post"
}
@pytest.fixture
def post(db,user) -> Post:
    return Post.objects.create(author=user,body="test post")
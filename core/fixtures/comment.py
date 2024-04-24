import pytest
from core.fixtures import user,post
from core.comment.models import Comment


@pytest.fixture
def comment(db,user,post):
    return Comment.objects.create(author=user,post=post,body="test comment")


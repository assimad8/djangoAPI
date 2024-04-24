from django.db import models
from core.abstract.models import AbstractManager,AbstractModel

# Create your models here.

class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    post = models.ForeignKey(to="core_post.Post",on_delete=models.PROTECT,related_name="comments")
    author = models.ForeignKey(to="core_user.User",on_delete=models.PROTECT,related_name="comments")
    body = models.TextField(blank=True,default="")
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return f"{self.author.name}"


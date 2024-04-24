from django.db import models
from core.abstract.models import AbstractModel,AbstractManager

# Create your models here.

class PostManager(AbstractManager):
    pass

class Post(AbstractModel):

    author = models.ForeignKey("core_user.User",on_delete=models.CASCADE,related_name="posts")   
    body = models.TextField()
    is_published = models.BooleanField(default=False)
    CATEGORY_CHOICES = [
        ('TECH', 'Technology'),
        ('ART', 'Art'),
        ('FOOD', 'Food'),
        ('TRAVEL', 'Travel'),
        ('OTHER', 'Other')
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')

    edited = models.BooleanField(choices=[(True,'Yes'),(False,'No')],default=False) 

    objects = PostManager()   

    def __str__(self):       
        return f"{self.author.name}"   
    class Meta:       
        db_table = "'core.post'"
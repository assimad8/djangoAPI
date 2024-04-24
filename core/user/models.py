import uuid
from django.db import models
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser,BaseUserManager
from core.abstract.models import AbstractManager,AbstractModel

class UserManager(BaseUserManager,AbstractManager):

    def create_user(self, email, username, password=None, **extra_fields):
            if not email:
                raise ValueError('The Email field must be set')
            if username is None:
                raise ValueError('The Username field must be set')
            if password  is None:
                raise ValueError('The Password field must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, username=username, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser,AbstractModel,PermissionsMixin):

    username = models.CharField(max_length=100,unique=True,db_index=True)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True)
    avatar = models.ImageField(upload_to="avatart/",default="avatar/default.png")
    bio = models.TextField(null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?212?\d{9}$|^0\d{9}$', message="Phone number must be entered in one of the following formats: '+212123456789', '+2120123456789', or '0123456789'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)  # validators should be a list
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    posts_liked = models.ManyToManyField("core_post.Post",related_name='liked_by')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def like(self,post):
        return self.posts_liked.add(post) 
    def remove_like(self,post):
        return self.posts_liked.remove(post) 
    def has_liked(self,post):
        return self.posts_liked.filter(pk=post.pk).exists()

    class Meta:
        # Add a unique related_name for groups
        # This will change the reverse accessor from 'groups' to 'custom_user_groups'
        permissions = [
            ("custom_permission", "Custom Permission"),
        ]
        abstract = False
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_permissions',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )
    groups = models.ManyToManyField(
    'auth.Group',
        related_name='user_groups',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    def __str__(self):
        return self.username
    @property   
    def name(self):       
        return f"{self.firstName} {self.lastName}"
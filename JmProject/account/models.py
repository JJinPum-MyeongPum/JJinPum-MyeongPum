from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=30, default='')
    profileImg = models.ImageField(upload_to="account/", blank=True, null=True)

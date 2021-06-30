from django.contrib.auth.models import AbstractUser
from django.contrib.auth import logout, authenticate
from django.db import models

# Create your models here.


class MyUser(AbstractUser):

    class Meta:
        verbose_name = '用户'




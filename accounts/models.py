from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    
    
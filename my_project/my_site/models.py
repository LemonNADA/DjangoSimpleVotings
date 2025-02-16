from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    about_oneself = models.CharField(max_length=500)

    REQUIRED_FIELDS = ["email", "city", "login", "password", "about_oneself"] 

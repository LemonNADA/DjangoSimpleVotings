from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    about_oneself = models.CharField(max_length=500)

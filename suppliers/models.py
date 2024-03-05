from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    tel = models.CharField(max_length=20, unique=True)
    niu = models.CharField(max_length=15, unique=True)
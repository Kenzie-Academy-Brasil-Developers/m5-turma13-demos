from django.db import models
from django.contrib.auth.models import AbstractUser

# MRO
class Account(AbstractUser):
    cpf = models.CharField(max_length=11, null=True)
    birthdate = models.DateField(null=True)
    email = models.EmailField(unique=True)
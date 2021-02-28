from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
	biografia = models.CharField(max_length = 1000, null = True)

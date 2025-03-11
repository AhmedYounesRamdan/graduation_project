from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser): # table for users
    is_craftsman = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)

    def __str__(self):
        return self.username


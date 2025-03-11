from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    profile_picture = models.ImageField(upload_to="user_profiles", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
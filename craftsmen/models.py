from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Craftsman(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="craftsmen", blank=True, null=True)
    service = models.ForeignKey(
        'services.Service',
        related_name='craftsmen',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

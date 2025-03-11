import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Service(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("service_detail", args=[str(self.id)])

    class Meta:
        permissions = [
            ('can_create_service', 'Can create service'),
            ('can_edit_service', 'Can edit service'),
            ('can_delete_service', 'Can delete service'),
        ]
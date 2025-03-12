from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

GOVERNORATE_CHOICES = [
    ('cairo', 'Cairo'),
    ('alexandria', 'Alexandria'),
    ('giza', 'Giza'),
    ('sharkia', 'Sharkia'),
    ('dakahlia', 'Dakahlia'),
    ('beheira', 'Beheira'),
    ('qalyubia', 'Qalyubia'),
    ('monufia', 'Monufia'),
    ('gharbia', 'Gharbia'),
    ('sohag', 'Sohag'),
    ('aswan', 'Aswan'),
    ('luxor', 'Luxor'),
    ('ismailia', 'Ismailia'),
    ('port_said', 'Port Said'),
    ('suez', 'Suez'),
    ('damietta', 'Damietta'),
    ('kafr_el_sheikh', 'Kafr El Sheikh'),
    ('matrouh', 'Matrouh'),
    ('north_sinai', 'North Sinai'),
    ('south_sinai', 'South Sinai'),
    ('red_sea', 'Red Sea'),
    ('new_valley', 'New Valley'),
    ('faiyum', 'Faiyum'),
    ('beni_suef', 'Beni Suef'),
    ('minya', 'Minya'),
    ('assiut', 'Assiut'),
    ('qena', 'Qena'),
]

class Craftsman(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to="craftsmen", blank=True, null=True)
    service = models.ForeignKey(
        'services.Service',
        related_name='craftsmen',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    bio = models.TextField(blank=True, null=True)
    governorate = models.CharField(max_length=50,choices=GOVERNORATE_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
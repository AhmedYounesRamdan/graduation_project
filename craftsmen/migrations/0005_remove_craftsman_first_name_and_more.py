# Generated by Django 4.0.10 on 2025-03-11 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('craftsmen', '0004_craftsman_certifications_craftsman_experience_years'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='craftsman',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='craftsman',
            name='last_name',
        ),
    ]

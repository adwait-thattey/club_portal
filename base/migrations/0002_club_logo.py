# Generated by Django 2.1.3 on 2019-01-15 11:04

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='logo',
            field=models.ImageField(blank=True, upload_to=base.models.club_logo_upload),
        ),
    ]

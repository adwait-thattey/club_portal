# Generated by Django 2.1.3 on 2018-12-28 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20181228_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='body',
        ),
    ]

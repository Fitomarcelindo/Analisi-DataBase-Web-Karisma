# Generated by Django 3.2.13 on 2022-07-27 11:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presence', '0004_userdata_nim'),
    ]

    operations = [
        migrations.AddField(
            model_name='classname',
            name='pr',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
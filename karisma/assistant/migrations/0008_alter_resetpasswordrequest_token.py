# Generated by Django 3.2.18 on 2023-03-13 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0007_auto_20230312_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpasswordrequest',
            name='token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assistant.tokentoresetpassword'),
        ),
    ]

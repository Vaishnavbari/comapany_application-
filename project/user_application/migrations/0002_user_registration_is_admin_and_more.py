# Generated by Django 5.0.6 on 2024-06-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]

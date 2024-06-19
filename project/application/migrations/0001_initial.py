# Generated by Django 5.0.6 on 2024-06-17 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='application_feature_category',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='application_role',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='applications',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='application_feature',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('is_active', models.BooleanField(default=True)),
                ('feature_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature_category_id', to='application.application_feature_category')),
            ],
        ),
        migrations.CreateModel(
            name='application_role_feature',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('is_active', models.BooleanField(default=True)),
                ('application_feature_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_feature_id', to='application.application_feature')),
                ('application_role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_role_id', to='application.application_role')),
            ],
        ),
        migrations.AddField(
            model_name='application_role',
            name='application_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application', to='application.applications'),
        ),
        migrations.AddField(
            model_name='application_feature_category',
            name='application_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_id', to='application.applications'),
        ),
        migrations.CreateModel(
            name='application_access',
            fields=[
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('access_type', models.CharField(max_length=50)),
                ('access_type_value', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_accessed', models.DateTimeField(auto_now_add=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
                ('application_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_application_id', to='application.applications')),
            ],
        ),
    ]

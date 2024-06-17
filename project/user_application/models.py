from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class user_registration(AbstractBaseUser) :
    id = models.IntegerField(primary_key=True, unique=True, default=1) 
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField()
    password = models.IntegerField()
    change_password = models.BooleanField()
    access_type = models.CharField(max_length=200)
    access_type_value = models.CharField(max_length=50)
    last_accessed = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD="username"
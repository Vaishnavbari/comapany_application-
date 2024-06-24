from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email , password, access_type, access_type_value,**extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not access_type:
            raise ValueError('Users must have an access type')
        if not access_type_value:
            raise ValueError('Users must have an access type value')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            access_type=access_type,
            access_type_value=access_type_value,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,  password, email=None , access_type=None, access_type_value=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            access_type='*',
            access_type_value="admin",
            **extra_fields
        )

        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class user_registration(AbstractBaseUser,PermissionsMixin) :
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    is_admin = models.BooleanField(default=False, blank=True, null=True)
    is_superuser = models.BooleanField(default=False, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)
    password = models.CharField(max_length=5000, blank=True, null=True)
    change_password = models.BooleanField(default=True, blank=True, null=True)
    access_type = models.CharField(max_length=200, blank=True, null=True)
    access_type_value = models.CharField(max_length=50, blank=True, null=True)
    last_accessed = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
     
    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ["email", "password"]

    def __str__(self):
        return self.email 

class Token(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.CASCADE)
    access_token = models.TextField(max_length=5000)
    refresh_token = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

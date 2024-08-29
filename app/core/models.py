"""
This module defines the custom user model and user manager for authentication.

It includes:
- UserManager: A custom manager for creating user and superuser accounts.
- User: A custom user model that uses email as the unique identifier and includes additional fields.
"""
from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):
    """Manager for user accounts."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """Create and return a superuser with an email and password."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractUser, PermissionsMixin):
    """Custom user model that uses email as the username field."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True, null=False, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

from pickle import TRUE
from tabnanny import verbose  # noqa: 401
from typing import Optional

from django.contrib.auth.models import AbstractBaseUser  # noqa: E501
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

from shared.django import TimeStampMixin

DEFAUL_ROLES = {
    "admin": 1,
    "user": 2,
}


class CustomUserManager(UserManager):
    """custom user manager"""

    def create_user(self, email, username=None, password=None, **kwargs):
        if not email:
            raise ValueError("Email field is required.")
        if not password:
            raise ValueError("Password field is required.")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self,
        email: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        **kwargs
    ):
        payload1: dict = {
            "is_superuser": True,
            "is_active": True,
            "is_staff": True,
            "role_id": DEFAUL_ROLES["admin"],
        }
        payload = {**kwargs, **payload1}

        return self.create_user(email, username, password, **payload)


class Role(TimeStampMixin):
    """ "Users role. Use fro giving permissions"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    """my custom model"""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone = models.CharField(max_length=13, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    role = models.ForeignKey(
        "Role",
        null=TRUE,
        default=DEFAUL_ROLES["user"],
        on_delete=models.SET_NULL,
        related_name="users",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = EMAIL_FIELD
    REQUIRED_FIELDS = []

    class Meta:
        # db_table = "users"
        verbose_name_plural = "users"

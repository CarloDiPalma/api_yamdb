from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_LEVEL_CHOICES = (
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("user", "User"),
    )
    role = models.CharField(
        'Роль',
        choices=USER_LEVEL_CHOICES,
        blank=True,
        default="user"
    ),
    bio = models.TextField(
        'Биография',
        null=True,
        blank=True,
        help_text='Биография'
    )

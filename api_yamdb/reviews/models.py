from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_LEVEL_CHOICES = (
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("user", "User"),
    )
    role = models.CharField(
        choices=USER_LEVEL_CHOICES,
        blank=True,
        default="user"
    ),
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name='Биография',
        help_text='Биография'
    )

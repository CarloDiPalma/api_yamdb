from django.contrib.auth.models import AbstractUser
from django.db import models

USER_ROLE = 'user'
MODERATOR_ROLE = 'moderator'
ADMIN_ROLE = 'admin'

ROLE_CHOICES = (
    (USER_ROLE, 'Пользователь'),
    (MODERATOR_ROLE, 'Модератор'),
    (ADMIN_ROLE, 'Администратор'),
)


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER_ROLE,
        blank=True
    )
    bio = models.TextField(
        verbose_name='Биография',
        max_length=1024,
        blank=True
    )
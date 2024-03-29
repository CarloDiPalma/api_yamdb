from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_ROLE = 'user'
    MODERATOR_ROLE = 'moderator'
    ADMIN_ROLE = 'admin'

    ROLE_CHOICES = (
        (USER_ROLE, 'Пользователь'),
        (MODERATOR_ROLE, 'Модератор'),
        (ADMIN_ROLE, 'Администратор'),
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER_ROLE,
        blank=True
    )
    confirmation_code = models.CharField(
        max_length=6,
        blank=True
    )
    bio = models.TextField(
        verbose_name='Биография',
        max_length=1024,
        blank=True
    )

    class Meta:
        ordering = ['-id']

    @property
    def is_admin(self):
        return self.is_staff or self.role == User.ADMIN_ROLE

    @property
    def is_moderator(self):
        return self.role == User.MODERATOR_ROLE

    @property
    def is_user(self):
        return self.role == User.USER_ROLE

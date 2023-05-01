from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def my_year_validator(value):
    if value > datetime.now().year:
        raise ValidationError(
            _(f'{value} - некорректный год!'),
            params={'value': value},
        )

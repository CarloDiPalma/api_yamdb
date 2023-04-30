from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

minimum_year = 1800


def my_year_validator(value):
    if value < minimum_year:
        raise ValidationError(
            _('%(value)s Некорректный год!'),
            params={'value': value},
        )

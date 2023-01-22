import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(username: str) -> None:
    pattern = re.compile(r"^[A-Za-z0-9_+-]+", re.IGNORECASE)

    if pattern.match(username).group() != username:
        raise ValidationError(
            _('Username can only contain letters, digits, "_" and "-"')
        )


def validate_person_name(name: str) -> None:
    if name is not None:
        pattern = re.compile(r"^[A-Za-z]+$", re.IGNORECASE)
        if pattern.match(name).group() != name:
            raise ValidationError(
                _('Your first and last name can only contain letters')
            )

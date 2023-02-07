from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re


def validate_title(title: str) -> None:
    pattern = re.compile(r'[A-Za-z0-9 _.,!"\'/$]*', re.IGNORECASE)
    if pattern.match(title).group() != title:
        raise ValidationError(
            _('Title should not contain any special characters')
        )


def validate_description(desc: str) -> None:
    if desc is not None:
        pattern = re.compile(r'[A-Za-z0-9 _.,!"\'/$]*', re.IGNORECASE)
        if pattern.match(desc).group() != desc:
            raise ValidationError(
                _('Description should not contain any special characters')
            )

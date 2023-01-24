from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .enums.family_status_enum import FamilyStatusChoice
from .managers import CustomUserManager
from .validators.custom_validation import validate_username, validate_person_name


FAMILYSTATUSCHOICES = [(status.name, status.value) for status in FamilyStatusChoice]


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True, null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=500, null=False)
    family_status = models.CharField(
        max_length=8, null=True,
        default=FamilyStatusChoice.single.value,
        choices=FAMILYSTATUSCHOICES, blank=True
    )
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    is_active = models.BooleanField(null=True, default=True, blank=True)
    pfp = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    is_staff = models.BooleanField(null=True, default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def clean(self):
        validate_username(self.username)
        validate_person_name(self.first_name)
        validate_person_name(self.last_name)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"

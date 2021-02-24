from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field.models import PhoneField


class CustomUser(AbstractUser):
    phone_number = PhoneField(blank=False, null=False)

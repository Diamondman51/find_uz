import re

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    phone_number = models.CharField(
        max_length=13, unique=True, blank=False, null=False,
        help_text='+998901234567',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USER_TYPE_CHOICES = (
        ('dict_user', 'Dict_user'),
    )
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES, null=True, blank=True)

    def clean(self):
        super().clean()
        reg = r'^\+?998[-\s]?(\d{2})[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})$'
        if not self.phone_number or not re.match(reg, self.phone_number):
            raise ValidationError({'phone_number': 'Phone number must be in the format +998901234567'})


class DictUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dict_user')
    dict_admin = models.BooleanField(default=False)

import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True, help_text='+998901234567')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def validate_phone_number(self):
        reg = r'^\+?998[-\s]?(\d{2})[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})$'
        if not re.match(reg, self.phone_number):
            raise ValidationError('Invalid phone number')
    
    def set_password(self, raw_password):
        if not raw_password.startswith('pbkdf2_sha'):
            return super().set_password(raw_password)
        return raw_password
    
    def save(self, *args, **kwargs):
        self.validate_phone_number()
        self.set_password(self.password)
        return super().save(*args, **kwargs)
    

class Address(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    

class Category(models.Model):
    name = models.CharField(max_length=100)


class ItemImages(models.Model):
    image = models.ImageField(upload_to='images/items/')
    item = models.ForeignKey('Items', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Item Image"
        verbose_name_plural = "Item Images"


class Items(models.Model):

    class StatusChoices(models.TextChoices):
        LOST = "lost", "Lost"
        FOUND = "found", "Found"
        CLAIMED = "claimed", "Claimed"
        RETURNED = "returned", "Returned"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.LOST, null=True, blank=True)
    latitude = models.FloatField(default=0.0, null=True, blank=True)
    longitude = models.FloatField(default=0.0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_lost_found = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

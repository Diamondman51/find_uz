from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True, help_text='+998901234567')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

class ItemImages(models.Model):
    image = models.ImageField(upload_to='images/items/')

class Items(models.Model):

    class StatusChoices(models.TextChoices):
        LOST = "lost", "Lost"
        FOUND = "found", "Found"
        CLAIMED = "claimed", "Claimed"
        RETURNED = "returned", "Returned"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    status = models.CharField(choices=StatusChoices.choices, default=StatusChoices.LOST)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    item_image = models.ForeignKey(ItemImages, on_delete=models.CASCADE)
    date_lost_found = models.DateTimeField()

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

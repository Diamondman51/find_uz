import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=13, unique=True, blank=True, null=True, help_text='+998901234567')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USER_TYPE_CHOICES = (
        ('dict_user', 'Dict_user'),
        ('find_uz_user', 'Find_uz_user'),
    )
    user_type = models.CharField(max_length=15, choices=USER_TYPE_CHOICES, null=True, blank=True)

    def clean(self):
        super().clean()
        reg = r'^\+?998[-\s]?(\d{2})[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})$'
        if not re.match(reg, self.phone_number):
            raise ValidationError({'phone_number': 'Phone number must be in the format +998901234567'})
    
    def set_password(self, raw_password):
        if not raw_password.startswith('pbkdf2_sha'):
            return super().set_password(raw_password)
        return raw_password
    
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(*args, **kwargs)


class DictUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class FindUzUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Address(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)
    

class Category(models.Model):
    name = models.CharField(max_length=100)


class ItemImages(models.Model):
    image = models.ImageField(upload_to='images/items/')
    item = models.ForeignKey('Items', on_delete=models.CASCADE, null=True, blank=True)

    def delete(self, using =None, keep_parents = False):
        self.image.delete()
        return super().delete(using, keep_parents)

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
    date_lost_found = models.DateField(null=True, blank=True)
    time_lost_found = models.TimeField(null=True, blank=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='message_sender', on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    receiver = models.ForeignKey(User, related_name='message_receiver', on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/messages/%Y/%m/%d')
    file = models.FileField(null=True, blank=True, upload_to='files/messages/%Y/%m/%d')

    def delete(self, using = None, keep_parents = False):
        self.file.delete()
        self.image.delete()
        return super().delete(using, keep_parents)

    def __str__(self):
        return f'{self.id}, {self.content}'


class MessageImage(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='messageimages', blank=None, null=None)
    image = models.ImageField(upload_to='images/messages/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def delete(self, using = None, keep_parents = False):
        self.image.delete()
        return super().delete(using, keep_parents)


class MessageFile(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='messagefiles', blank=None, null=None)
    file = models.FileField(upload_to='files/messages/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def delete(self, using = None, keep_parents = False):
        self.file.delete()
        return super().delete(using, keep_parents)


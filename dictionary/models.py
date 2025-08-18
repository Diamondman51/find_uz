import datetime
from django.db import models

from api.models import User

# Create your models here.


class DiplomaticTerm(models.Model):
    title = models.CharField(max_length=255, unique=True, )
    definition = models.TextField()
    related_terms = models.ManyToManyField('self', blank=True, )
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )
    categories = models.ManyToManyField('Category', blank=True, )
    related_countries = models.ManyToManyField('Country', blank=True, )
    sources = models.ManyToManyField('Source', blank=True, )
    photo_id = models.ManyToManyField('DiplomaticTermPhoto', blank=True, )
    created_at = models.DateTimeField(auto_now_add=True, null=True, )
    updated_at = models.DateTimeField(auto_now=True, null=True, )

    def __str__(self):
        return self.title


class DiplomaticTermPhoto(models.Model):
    photo = models.ImageField(upload_to='images/terms/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f'{self.photo.path}'
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    iso_code = models.CharField(max_length=3, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Source(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    publication_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

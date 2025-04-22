from django.db import models

# Create your models here.


class DiplomaticTerm(models.Model):
    title = models.CharField(max_length=255, unique=True)
    definition = models.TextField()
    related_terms = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    related_countries = models.ManyToManyField('Country', blank=True)
    sources = models.ManyToManyField('Source', blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    iso_code = models.CharField(max_length=3, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Source(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

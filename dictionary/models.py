from django.db import models


class DiplomaticTerm(models.Model):
    title = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='images/terms/', blank=True, null=True)
    definition = models.TextField()
    related_terms = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    related_countries = models.ManyToManyField('Country', blank=True)
    sources = models.ManyToManyField('Source', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['-updated_at']),
            models.Index(fields=['category']),
        ]

    def delete(self, using=None, keep_parents=False):
        if self.photo:
            try:
                self.photo.delete(save=False)
            except (ValueError, FileNotFoundError):
                pass
        return super().delete(using, keep_parents)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    iso_code = models.CharField(max_length=3, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class Source(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(blank=True, null=True)
    publication_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-publication_date']
        indexes = [
            models.Index(fields=['-publication_date']),
        ]

    def __str__(self):
        return self.title

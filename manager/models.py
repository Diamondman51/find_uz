from django.db import models

# Create your models here.

class App(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    start = models.TimeField()
    end = models.TimeField()
    for_whom = models.CharField(max_length=100, blank=False, null=False)
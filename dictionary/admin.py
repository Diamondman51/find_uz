from django.contrib import admin

from dictionary.models import Category, Country, DiplomaticTerm, Source

# Register your models here.

admin.site.register(DiplomaticTerm)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Source)

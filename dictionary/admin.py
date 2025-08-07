from django.contrib import admin

from dictionary.models import Category, Country, DiplomaticTerm, DiplomaticTermPhoto, Source

# Register your models here.

admin.site.register(DiplomaticTerm)
admin.site.register(DiplomaticTermPhoto)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Source)

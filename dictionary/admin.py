from django.contrib import admin

from dictionary.models import Category, Country, DiplomaticTerm, DiplomaticTermPhoto, Source

# Register your models here.

class DiplomaticTermAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']


class DiplomaticTermPhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'created_at', 'updated_at']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']


class SourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'created_at', 'updated_at']


admin.site.register(DiplomaticTerm, DiplomaticTermAdmin)
admin.site.register(DiplomaticTermPhoto, DiplomaticTermPhotoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Source, SourceAdmin)

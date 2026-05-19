from django.contrib import admin

from dictionary.models import Category, Country, DiplomaticTerm, Source


@admin.register(DiplomaticTerm)
class DiplomaticTermAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'related_countries')
    search_fields = ('title', 'definition')
    autocomplete_fields = ('category', 'related_countries', 'sources', 'related_terms')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'iso_code', 'created_at')
    search_fields = ('name', 'iso_code')


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_date', 'created_at')
    list_filter = ('publication_date',)
    search_fields = ('title',)

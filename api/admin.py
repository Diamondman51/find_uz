from django.contrib import admin

from api.models import DictUser, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'user_type', 'created_at', 'updated_at')
    list_display_links = ('id', 'username', 'email')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    ordering = ('username',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('username', 'email', 'phone_number')


@admin.register(DictUser)
class DictUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dict_admin')
    list_filter = ('dict_admin',)
    autocomplete_fields = ('user',)

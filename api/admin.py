from django.contrib import admin

from api.models import *

class ItemImagesInline(admin.StackedInline):
    model = ItemImages
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesInline]
    list_display = ('user', 'status', 'date_lost_found')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username', 'email')
    ordering = ('username',)



# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ItemImages)
admin.site.register(Items, ItemAdmin)
admin.site.register(Category)

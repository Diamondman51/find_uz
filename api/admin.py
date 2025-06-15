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


class ItemImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_f', 'image')

    def item_f(self, obj):
        return obj.item.item_name


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'content', 'created_at', 'image', 'file']


class MessageImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_f', 'image']
    list_display_links = ['id', 'message_f']

    def message_f(self, obj):
        return obj.message.id


class MessageFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_f', 'file']
    list_display_links = ['id', 'message_f']

    def message_f(self, obj):
        return obj.message.id
    

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ItemImages, ItemImagesAdmin)
admin.site.register(Items, ItemAdmin)
admin.site.register(Category)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageImage, MessageImageAdmin)
admin.site.register(MessageFile, MessageFileAdmin)

from django.contrib import admin

from api.models import (
    DictUser,
    FindUzUser,
    ItemImages,
    Items,
    Message,
    MessageFile,
    MessageImage,
    User,
)


class ItemImagesInline(admin.StackedInline):
    model = ItemImages
    extra = 0


@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesInline]
    list_display = ('user', 'status', 'date_lost_found')
    list_filter = ('status',)
    search_fields = ('item_name', 'description', 'user__username')


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


@admin.register(FindUzUser)
class FindUzUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    autocomplete_fields = ('user',)


@admin.register(ItemImages)
class ItemImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_f', 'image')

    def item_f(self, obj):
        return obj.item.item_name if obj.item else None


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'receiver', 'content', 'created_at']
    search_fields = ('content', 'sender__username', 'receiver__username')


@admin.register(MessageImage)
class MessageImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_f', 'image']
    list_display_links = ['id', 'message_f']

    def message_f(self, obj):
        return obj.message.id


@admin.register(MessageFile)
class MessageFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_f', 'file']
    list_display_links = ['id', 'message_f']

    def message_f(self, obj):
        return obj.message.id

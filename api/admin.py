import datetime
from django import forms
from django.contrib import admin

from api.models import *

class ItemImagesInline(admin.StackedInline):
    model = ItemImages
    extra = 0


class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImagesInline]
    list_display = ('user', 'status', 'date_lost_found')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'username', 'email')
    ordering = ('username',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ["username", "email", "phone_number"]


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
    

class DictUserForm(forms.ModelForm):
    # expose User fields
    username = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    # updated_at = forms.DateTimeField(disabled=True, required=False)
    # created_at = forms.DateTimeField(disabled=True, required=False)
    class Meta:
        model = DictUser
        fields = ('user', "dict_admin", "username", "email", "phone_number", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and getattr(self.instance, 'user', None):
            self.fields["username"].initial = self.instance.user.username
            self.fields["email"].initial = self.instance.user.email
            self.fields["phone_number"].initial = self.instance.user.phone_number
            self.fields["first_name"].initial = self.instance.user.first_name
            self.fields["last_name"].initial = self.instance.user.last_name

    def save(self, commit=True):
        dict_user: DictUser = super().save(commit=False)
        user = dict_user.user
        print(f'{self.cleaned_data=}')
        # update user fields from form
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            dict_user.save()
        return dict_user


class DictUserAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    readonly_fields = ['user__created_at', 'user__updated_at']
    form = DictUserForm
    list_display = ['id', 'dict_admin', 'username', 'email', 'phone_number', 'user']
    list_display_links = ['id', 'dict_admin', 'username',]


    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email

    def phone_number(self, obj):
        return obj.user.phone_number


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(FindUzUser,)
admin.site.register(DictUser, DictUserAdmin)
admin.site.register(ItemImages, ItemImagesAdmin)
admin.site.register(Items, ItemAdmin)
admin.site.register(Category)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageImage, MessageImageAdmin)
admin.site.register(MessageFile, MessageFileAdmin)

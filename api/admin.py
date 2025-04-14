from django.contrib import admin

from api.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(ItemImages)
admin.site.register(Items)
admin.site.register(Category)
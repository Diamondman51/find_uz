from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import *

router = DefaultRouter()
router.register('user_view', UserView, basename='user_view')
router.register('user_create_view', UserCreateView, basename='user_create_view')
# router.register()
router.register('admin_user_view', AdminUserView, basename='admin_user_view')
router.register('items_view', ItemsView, basename='items_view')


urlpatterns = [
    # path('userview/', UserView.as_view(), name='userview'),
    path('delete_user/', UserDeleteView.as_view({'delete': 'my_destroy'}), name='user_delete_view')
] + router.urls

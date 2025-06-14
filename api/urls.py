from rest_framework.routers import DefaultRouter

from api.models import MessageFile
from api.views import *

router = DefaultRouter()
router.register('user_view', UserView, basename='user_view')
router.register('user_create_view', UserCreateView, basename='user_create_view')
router.register('admin_user_view', AdminUserView, basename='admin_user_view')
router.register('items_view', ItemsView, basename='items_view')
router.register('item_images_view', ItemImagesView, 'item_images_view')
router.register('items_images_edit_view', ItemImagesAuthenticatedView)
router.register('items_edit_view', ItemsAuthenticatedView)
router.register('message_view', MessageView, 'message_view')
router.register('edit_message_view', EditMessageView, 'edit_message_view')
router.register('create_message_view', CreateMessageView, 'create_message_view')
router.register('message_files_view', MessageFilesView, 'message_files_view')
router.register('message_images_view', MessageImagesView, 'message_images_view')

urlpatterns = [
] + router.urls

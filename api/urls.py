from rest_framework.routers import DefaultRouter

from api.views import (
    AdminUserView,
    CreateMessageView,
    EditMessageView,
    ItemImagesAuthenticatedView,
    ItemImagesView,
    ItemsAuthenticatedView,
    ItemsView,
    MessageFilesView,
    MessageImagesView,
    MessageView,
    UserCreateView,
    UserView,
)


router = DefaultRouter()
router.register('user_view', UserView, basename='user_view')
router.register('user_create_view', UserCreateView, basename='user_create_view')
router.register('admin_user_view', AdminUserView, basename='admin_user_view')
router.register('items_view', ItemsView, basename='items_view')
router.register('item_images_view', ItemImagesView, basename='item_images_view')
router.register('items_images_edit_view', ItemImagesAuthenticatedView, basename='items_images_edit_view')
router.register('items_edit_view', ItemsAuthenticatedView, basename='items_edit_view')
router.register('message_view', MessageView, basename='message_view')
router.register('edit_message_view', EditMessageView, basename='edit_message_view')
router.register('create_message_view', CreateMessageView, basename='create_message_view')
router.register('message_files_view', MessageFilesView, basename='message_files_view')
router.register('message_images_view', MessageImagesView, basename='message_images_view')

urlpatterns = router.urls

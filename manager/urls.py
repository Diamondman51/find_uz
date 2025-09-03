from rest_framework.routers import DefaultRouter

from manager.views import AppView

router = DefaultRouter()

router.register('apps', AppView, 'apps')

urlpatterns = [] + router.urls
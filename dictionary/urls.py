from rest_framework.routers import DefaultRouter

from dictionary.views import CategoryView, CreateCategoryView, CreateDiplomaticTermView, DiplomaticTermView 

router = DefaultRouter()

router.register('term', DiplomaticTermView, basename='diplomatic_term')
router.register('category', CategoryView, basename='category')
router.register('create_term', CreateDiplomaticTermView, basename='create_term')
router.register('create_category', CreateCategoryView, basename='create_category')

urlpatterns = [] + router.urls

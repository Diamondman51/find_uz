from rest_framework.routers import DefaultRouter

from dictionary.views import CategoryView, CountryView, CreateCategoryView, CreateDiplomaticTermView, DiplomaticTermPhotoView, DiplomaticTermView, SourceView, UserCreateView 

router = DefaultRouter()

router.register('term', DiplomaticTermView, basename='diplomatic_term')
router.register('category', CategoryView, basename='category')
router.register('create_term', CreateDiplomaticTermView, basename='create_term')
router.register('create_category', CreateCategoryView, basename='create_category')
router.register('user_create', UserCreateView, basename='user_create')
router.register('term_photo', DiplomaticTermPhotoView, basename='term_photo')
router.register('source', SourceView, basename='source')
router.register('country', CountryView, basename='country')

urlpatterns = [] + router.urls

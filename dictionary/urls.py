from rest_framework.routers import DefaultRouter

from dictionary.views import CategoryView, ContactAdminView, ContactView, CountryAdminView, CountryView, CreateCategoryView, CreateDiplomaticTermView, DiplomaticTermPhotoAdminView, DiplomaticTermPhotoView, DiplomaticTermView, SearchTermView, SourceAdminView, SourceView, UserCreateView 

router = DefaultRouter()

router.register('term', DiplomaticTermView, basename='diplomatic_term')
router.register('search_term', SearchTermView, basename='search_term')
router.register('create_term', CreateDiplomaticTermView, basename='create_term')
router.register('category', CategoryView, basename='category')
router.register('create_category', CreateCategoryView, basename='create_category')
router.register('user_create', UserCreateView, basename='user_create')
router.register('term_photo_admin', DiplomaticTermPhotoAdminView, basename='term_photo_admin')
router.register('term_photo', DiplomaticTermPhotoView, basename='term_photo')
router.register('source_admin', SourceAdminView, basename='source_admin')
router.register('source', SourceView, basename='source')
router.register('country_admin', CountryAdminView, basename='country_admin')
router.register('country', CountryView, basename='country')
router.register('contact', ContactView, basename='contact')
router.register('contact_admin', ContactAdminView, basename='contact_admin')

urlpatterns = [] + router.urls

from api.models import DictUser
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from api.serializers import UserSerializer
from dictionary.models import Category, Contact, Country, DiplomaticTerm, DiplomaticTermPhoto, Source
from dictionary.permissions import IsAdmin
from dictionary.serializers import CategorySerializer, ContactSerializer, CountrySerializer, DictUserSerializer, DiplomaticTermDetailSerializer, DiplomaticTermPhotoSerializer, DiplomaticTermReadSerializer, DiplomaticTermWriteSerializer, SourceSerializer


# Create your views here.

class DictUserView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DictUser.objects.select_related('user')
    serializer_class = DictUserSerializer
    permission_classes = [IsAuthenticated]
    

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        return Response('You do not have required permission')

    def partial_update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().partial_update(request, *args, **kwargs)
        return Response('You do not have required permission')

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        return Response('You do not have required permission')
    
    def list(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.dict_user.dict_admin:
            q = DictUser.objects.exclude(user=request.user.id)
            ser = self.get_serializer(q, many=True)
            return Response(ser.data)
        return Response('You do not have required permission')
    
    def retrieve(self, request, *args, **kwargs):    
        if request.user.is_superuser or request.user.dict_user.dict_admin:
            return super().retrieve(request, *args, **kwargs)
        return Response('You do not have required permission')
    
    
class DiplomaticTermView(mixins.ListModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    # prefetch_related(
    #     'related_terms',
    #     'categories',
    #     'related_countries',
    #     'sources',
    #     'photo_id',
    # )
    serializer_class = DiplomaticTermReadSerializer

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DiplomaticTermDetailView(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    # prefetch_related(
    #     'related_terms',
    #     'categories',
    #     'related_countries',
    #     'sources',
    #     'photo_id',
    # )
    serializer_class = DiplomaticTermDetailSerializer


class SearchTermView(mixins.ListModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    serializer_class = DiplomaticTermReadSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title',]


class CreateDiplomaticTermView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.prefetch_related(
        'related_terms',
        'categories',
        'related_countries',
        'sources',
        'photo_id',
    )

    serializer_class = DiplomaticTermWriteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    
    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ser = DiplomaticTermDetailSerializer(instance)
        return Response(ser.data)
    
    def create(self, request, *args, **kwargs):
        serializer = DiplomaticTermWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DiplomaticTermPhotoAdminView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = DiplomaticTermPhoto.objects.all()
    serializer_class = DiplomaticTermPhotoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class DiplomaticTermPhotoView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DiplomaticTermPhoto.objects.all()
    serializer_class = DiplomaticTermPhotoSerializer


class CountryAdminView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class CountryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SourceAdminView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class SourceView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategoryView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save(user_type='dict_user')
        res = self.get_serializer(user)
        return Response(res.data, status=status.HTTP_201_CREATED)


class ContactView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactAdminView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]

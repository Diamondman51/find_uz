from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from api.serializers import UserSerializer
from dictionary.models import Category, Country, DiplomaticTerm, DiplomaticTermPhoto, Source
from dictionary.serializers import CategorySerializer, CountrySerializer, DiplomaticTermPhotoSerializer, DiplomaticTermSerializer, SourceSerializer


# Create your views here.

class DiplomaticTermView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    serializer_class = DiplomaticTermSerializer


class DiplomaticTermPhotoView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = DiplomaticTermPhoto.objects.all()
    serializer_class = DiplomaticTermPhotoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class CountryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class SourceView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class CreateDiplomaticTermView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    serializer_class = DiplomaticTermSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategoryView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        # print(f'{request.headers=}')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save(user_type='dict_user')
        res = self.get_serializer(user)
        return Response(res.data, status=status.HTTP_201_CREATED)

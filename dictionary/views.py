from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Category
from dictionary.models import DiplomaticTerm
from dictionary.serializers import DiplomaticTermSerializer


# Create your views here.

class DiplomaticTermView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    serializer_class = DiplomaticTermSerializer


class CreateDiplomaticTermView(mixins.CreateModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    serializer_class = DiplomaticTermSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = DiplomaticTermSerializer


class CreateCategoryView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = DiplomaticTermSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]

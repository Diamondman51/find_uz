from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.serializers import UserSerializer
from dictionary.models import Category, DiplomaticTerm
from dictionary.permissions import IsSuperuserOrDictAdmin
from dictionary.serializers import (
    CategorySerializer,
    DiplomaticTermDetailSerializer,
    DiplomaticTermReadSerializer,
    DiplomaticTermWriteSerializer,
)
from dictionary.throttles import DictionaryAnonSlidingThrottle, DictionaryUserSlidingThrottle


DETAIL_PREFETCH = ('related_terms', 'related_countries', 'sources')
DETAIL_SELECT = ('category',)
# Columns actually used by DiplomaticTermReadSerializer; .only() skips the
# heavy `definition` TextField on list responses.
LIST_ONLY = ('id', 'title', 'photo', 'created_at', 'updated_at')


class DiplomaticTermView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    throttle_classes = [DictionaryAnonSlidingThrottle]

    def get_queryset(self):
        if self.action == 'retrieve':
            return (
                DiplomaticTerm.objects
                .select_related(*DETAIL_SELECT)
                .prefetch_related(*DETAIL_PREFETCH)
            )
        return DiplomaticTerm.objects.only(*LIST_ONLY).order_by('-created_at')

    def get_serializer_class(self):
        return DiplomaticTermDetailSerializer if self.action == 'retrieve' else DiplomaticTermReadSerializer


class CreateDiplomaticTermView(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet,
):
    queryset = DiplomaticTerm.objects.all()
    serializer_class = DiplomaticTermWriteSerializer
    permission_classes = [IsSuperuserOrDictAdmin]
    authentication_classes = [JWTAuthentication]
    throttle_classes = [DictionaryUserSlidingThrottle]


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    throttle_classes = [DictionaryAnonSlidingThrottle]


class CreateCategoryView(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet,
):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsSuperuserOrDictAdmin]
    authentication_classes = [JWTAuthentication]
    throttle_classes = [DictionaryUserSlidingThrottle]


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    throttle_classes = [DictionaryAnonSlidingThrottle]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(user_type='dict_user')
        return Response(self.get_serializer(user).data, status=status.HTTP_201_CREATED)

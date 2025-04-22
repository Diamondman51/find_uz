
import inspect
import asgiref
import asgiref.sync
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from adrf import mixins
from adrf.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError
from adrf.viewsets import ViewSet
from rest_framework import status
from rest_framework.decorators import action

from api.models import Items, User
from api.permissions import IsOwner
from api.serializers import ItemsSerializer, UserSerializer
# Create your views here.


# class UserView(ListAPIView, CreateAPIView, GenericAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = [JWTAuthentication, SessionAuthentication]
#     permission_classes = [IsAuthenticated]


class UserView(mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]

    
    async def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser or user.is_staff:
            return await asgiref.sync.sync_to_async(super().list)(request, *args, **kwargs)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    async def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserDeleteView(ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]

    @action(methods=['delete'], url_path='delete_user', detail=False)
    async def my_destroy(self, request, *args, **kwargs):
        print('Nothing')
        await request.user.adelete()
        return Response({'detail': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AdminUserView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class ItemsView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer
    authentication_classes = [JWTAuthentication, BasicAuthentication]


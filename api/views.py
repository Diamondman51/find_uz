from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from django.db.models import Prefetch

from django.db.models import Q
from api.models import ItemImages, Items, Message, MessageFile, MessageImage, User
from api.permissions import IsOwner
from api.serializers import CreateMessageSerializer, ItemImagesSerializer, ItemsSerializer, MessageFilesSerializer, MessageImagesSerializer, MessageSerializer, UserSerializer
# Create your views here.

class UserView(mixins.UpdateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.filter(user_type='find_uz_user')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


    def list(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser or user.is_staff:
            return super().list(request, *args, **kwargs)
        # serializer = self.get_serializer(user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(request.data)
        ser.is_valid(raise_exception=True)
        ser.save(user_type='find_uz_user')
        res = self.get_serializer(ser)
        return Response(res.data, status=status.HTTP_201_CREATED)


class AdminUserView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.filter(user_type='find_uz_user')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication, BasicAuthentication]

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser = ser.save(user_type='find_uz_user')
        res = self.get_serializer(ser)
        return Response(res.data, status=status.HTTP_201_CREATED)


class ItemsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Items.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ItemsSerializer


class ItemsAuthenticatedView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Items.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ItemsSerializer


class ItemImagesAuthenticatedView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = ItemImages.objects.all()
    serializer_class = ItemImagesSerializer

    def partial_update(self, request, *args, **kwargs):
        instance: ItemImages = self.get_object()
        image = request.data.get('image', False)
        if image:
            try:
                instance.image.delete()
            except:
                pass
        return super().partial_update(request, *args, **kwargs)


class ItemImagesView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    queryset = ItemImages.objects.all()
    serializer_class = ItemImagesSerializer


class MessageView(mixins.ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        print('Hello')
        return Message.objects.filter(
            Q(sender=self.request.user) | Q(receiver=self.request.user)
        ).prefetch_related(Prefetch('messageimages', queryset=MessageImage.objects.all()),
                           Prefetch('messagefiles', queryset=MessageFile.objects.all()))


class EditMessageView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


class CreateMessageView(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


class MessageFilesView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MessageFile.objects.all()
    serializer_class = MessageFilesSerializer

    def get_queryset(self):
        return MessageFile.objects.filter(
            Q(message__sender=self.request.user) | Q(message__receiver=self.request.user)
        )
    

class MessageImagesView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MessageImage.objects.all()
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    serializer_class = MessageImagesSerializer


    def list(self, request, *args, **kwargs):
        print(f'{request.headers=}')
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        return MessageImage.objects.filter(
            Q(message__sender=self.request.user) | Q(message__receiver=self.request.user)
        )


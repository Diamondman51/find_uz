from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from manager.models import App
from manager.ser import AppSer
# Create your views here.

class AppView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = App.objects.all()
    serializer_class = AppSer
    permission_classes = [AllowAny]
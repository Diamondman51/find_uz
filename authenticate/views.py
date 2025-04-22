from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView

from authenticate.ser import UserTokenSerializer

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenSerializer


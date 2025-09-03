from rest_framework.serializers import ModelSerializer

from manager.models import App

class AppSer(ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"
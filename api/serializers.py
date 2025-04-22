from rest_framework import serializers

from api.models import Items, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['user', 'item_name', 'category', 'status', 'created_at', 'date_lost_found']

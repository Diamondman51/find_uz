import re
from rest_framework import serializers
from api.models import ItemImages, Items, Message, MessageFile, MessageImage, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}, "user_type": {"read_only": True}}

    def validate_phone_number(self, phone_number):
        reg = r'^\+?998[-\s]?(\d{2})[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})$'
        if not re.match(reg, phone_number):
            raise serializers.ValidationError("Invalid phone number")
        
        return phone_number


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'user', 'item_name', 'category', 'status', 'date_lost_found', 'time_lost_found', 'color', 'brand', 'longitude', 'latitude']


class ItemImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImages
        fields = ['id', 'item', 'image']


class MessageImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageImage
        fields = ['id', 'message', 'image']


class MessageFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageFile
        fields = ['id', 'message', 'file']


class MessageSerializer(serializers.ModelSerializer):

    messageimages = MessageImagesSerializer(many=True, read_only=True, required=False)
    messagefiles = MessageFilesSerializer(many=True, read_only=True, required=False)

    # messageimages = serializers.SerializerMethodField()
    # messagefiles = serializers.SerializerMethodField()        

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'image', 'file', 'messageimages', 'messagefiles']
        # extra_kwargs = {"messageimages": {'write_only': True}, "messagefiles": {'write_only': True}}


class CreateMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'image', 'file']
        
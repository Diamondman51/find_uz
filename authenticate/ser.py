from xml.dom import ValidationErr
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.serializers import ValidationError
from api.models import User


class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        try:
            user_type = getattr(user, 'user_type')
            token['user_type'] = user_type
            return token
        except AttributeError:
            return ValidationErr('User does not have required attribute')


    def validate(self, attrs):
        attrs['username'] = attrs.get('phone', attrs.get('username'))
        try:
            user = super().validate(attrs)
        except User.DoesNotExist:
            raise ValidationError({'error': 'User does not exist'}, code=400)
        return user

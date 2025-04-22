from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.serializers import ValidationError
from api.models import User


class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        return super().get_token(user)

    def validate(self, attrs):
        attrs['username'] = attrs.get('phone', attrs.get('username'))
        try:
            data = super().validate(attrs)
        except User.DoesNotExist:
            raise ValidationError({'error': 'User does not exist'}, code=400)
        return data
    
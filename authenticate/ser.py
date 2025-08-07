import logging
from xml.dom import ValidationErr
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.serializers import ValidationError
from api.models import User

logger = logging.getLogger(__name__)

class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token


    def validate(self, attrs):
        attrs['username'] = attrs.get('phone', attrs.get('username'))
        try:
            user = super().validate(attrs)
            user_type = getattr(self.user, 'user_type')
            user['user_type'] = user_type
        except User.DoesNotExist:
            raise ValidationError({'error': 'User does not exist'}, code=400)
        return user

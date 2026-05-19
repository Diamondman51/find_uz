from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Allow clients to send `phone` in place of `username`.
        if 'phone' in attrs and not attrs.get('username'):
            attrs['username'] = attrs.pop('phone')
        data = super().validate(attrs)
        data['user_type'] = getattr(self.user, 'user_type', None)
        return data

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class PhoneNumberAuthentication(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        try:
            user = User.objects.get(phone_number=username)
            print(f'{user=}, {username=}')
            last = username[-1]
            if last.isdigit():
                user = User.objects.get(phone_number=username)
                print(user.check_password(password))
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            print(True)
            return user
        return None

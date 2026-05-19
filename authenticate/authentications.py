from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class PhoneNumberAuthentication(ModelBackend):
    """Authenticate by phone_number if the credential looks like a phone
    (ends in a digit), otherwise by username. The original implementation
    always queried phone_number first and silently rejected username logins."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or password is None:
            return None
        try:
            if username[-1:].isdigit():
                user = User.objects.get(phone_number=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

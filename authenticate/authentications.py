import re

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

# Matches +998..., 998..., or any string that looks like a phone (starts with +
# or digits). Usernames like "admin1" no longer get mis-routed to phone lookup.
_PHONE_RE = re.compile(r'^\+?\d+$')


class PhoneNumberAuthentication(ModelBackend):
    """Authenticate by phone_number if the credential matches a phone-like
    pattern (digits, optional leading +), otherwise by username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or password is None:
            return None
        try:
            if _PHONE_RE.match(username):
                user = User.objects.get(phone_number=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

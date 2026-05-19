from rest_framework.permissions import BasePermission


def _is_dict_admin(user):
    dict_user = getattr(user, 'dict_user', None)
    return bool(dict_user and dict_user.dict_admin)


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not getattr(user, 'is_authenticated', False):
            return False
        return _is_dict_admin(user)


class IsSuperuserOrDictAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not getattr(user, 'is_authenticated', False):
            return False
        return bool(user.is_superuser or _is_dict_admin(user))

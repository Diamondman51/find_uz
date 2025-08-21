from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print(f'{request.user.__dict__=}')
        if not request.user.dict_user:
            return False
        return request.user.dict_user.dict_admin
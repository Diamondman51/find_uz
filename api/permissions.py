from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
        
    def has_object_permission(self, request, view, obj):
        print(request.user.username, obj.username)
        
        return True
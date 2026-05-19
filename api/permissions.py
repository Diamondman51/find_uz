from rest_framework.permissions import BasePermission

from api.models import ItemImages, Items, Message, MessageFile, MessageImage, User


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User):
            return request.user == obj

        if isinstance(obj, Items):
            return request.user == obj.user

        if isinstance(obj, ItemImages):
            return obj.item is not None and request.user == obj.item.user

        if isinstance(obj, Message):
            return request.user == obj.sender or request.user == obj.receiver

        if isinstance(obj, MessageImage):
            return request.user == obj.message.sender or request.user == obj.message.receiver

        if isinstance(obj, MessageFile):
            return request.user == obj.message.sender or request.user == obj.message.receiver

        return False

from rest_framework.permissions import BasePermission

from api.models import ItemImages, Message, MessageFile, MessageImage, User

class IsOwner(BasePermission):

    def has_permission(self, request, view):
        print(f"IsOwner.has_permission called for user: {request.user.username}")
    #     # For has_permission, if you just want to defer to has_object_permission
    #     # for detail views, simply return True here.
    #     # Otherwise, add general checks for list views.
        return True
        
    def has_object_permission(self, request, view, obj):
        print('Hello:', request.user.username)
        
        if isinstance(obj, User):
            return request.user == obj
        
        if isinstance(obj, ItemImages):
            return request.user == obj.item.user
        
        if isinstance(obj, Message):
            obj: Message = obj
            return request.user == obj.sender or request.user == obj.receiver
        
        if isinstance(obj, MessageImage):
            obj: MessageImage = obj
            return request.user == obj.message.sender or request.user == obj.message.receiver

        if isinstance(obj, MessageFile):
            obj: MessageFile = obj
            return request.user == obj.message.sender or request.user == obj.message.receiver

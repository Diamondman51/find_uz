from api.models import DictUser
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from api.serializers import UserSerializer
from dictionary.models import Category, Contact, Country, DiplomaticTerm, DiplomaticTermPhoto, Source
from dictionary.serializers import CategorySerializer, ContactSerializer, CountrySerializer, DictUserSerializer, DiplomaticTermDetailSerializer, DiplomaticTermPhotoSerializer, DiplomaticTermReadSerializer, DiplomaticTermWriteSerializer, SourceSerializer


# Create your views here.

class DictUserView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    r'''destroy
: This method is used to delete a 
DictUser
 instance. Only superusers can delete a 
DictUser
. If the request user is not a superuser, a response with status code 403 and a message "You do not have required permission" is returned.
partial_update
: This method is used to partially update a 
DictUser
 instance. Only superusers can partially update a 
DictUser
e:\find_uz\dictionary\views.py
. If the request user is not a superuser, a response with status code 403 and a message "You do not have required permission" is returned.
update
: This method is used to update a 
DictUser
 instance. Only superusers can update a 
DictUser
. If the request user is not a superuser, a response with status code 403 and a message "You do not have required permission" is returned.
list
: This method is used to list all 
DictUser
 instances excluding the current user. Only superusers and dict_admins can list all 
DictUser
 instances. If the request user is not a superuser or dict_admin, a response with status code 403 and a message "You do not have required permission" is returned.
retrieve
: This method is used to retrieve a 
DictUser
 instance. Only superusers and dict_admins can retrieve a 
DictUser
 instance. If the request user is not a superuser or dict_admin, a response with status code 403 and a message "You do not have required permission" is returned.'''
    queryset = DictUser.objects.select_related('user')
    serializer_class = DictUserSerializer
    permission_classes = [IsAuthenticated]
    

    def destroy(self, request, *args, **kwargs):
        """
    Destroy a DictUser instance.
    Only superusers can delete a DictUser. If the request user is not a superuser,
    a response with status code 403 and a message "You do not have required permission"
    is returned.
    Parameters:
        request (Request): The request containing the user and other relevant data.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        Response: A response containing the result of the delete operation.
        """
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        return Response('You do not have required permission')

    def partial_update(self, request, *args, **kwargs):
        """
        Partially update a DictUser instance.
        Only superusers can partially update a DictUser. If the request user is not a superuser,
        a response with status code 403 and a message "You do not have required permission"
        is returned.
        Parameters:
            request (Request): The request containing the user and other relevant data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: A response containing the result of the partial update operation.
        """
        if request.user.is_superuser:
            return super().partial_update(request, *args, **kwargs)
        return Response('You do not have required permission')

    def update(self, request, *args, **kwargs):
        """
        Update a DictUser instance.
        Only superusers can update a DictUser. If the request user is not a superuser,
        a response with status code 403 and a message "You do not have required permission"
        is returned.
        Parameters:
            request (Request): The request containing the user and other relevant data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: A response containing the result of the update operation.
        """
        if request.user.is_superuser:
            return super().update(request, *args, **kwargs)
        return Response('You do not have required permission')
    
    def list(self, request, *args, **kwargs):
        """
        List all DictUser instances excluding the current user.
        Only superusers and dict_admins can list all DictUser instances.
        If the request user is not a superuser or dict_admin, a response with status code 403 and a message
        "You do not have required permission" is returned.
        Parameters:
            request (Request): The request containing the user and other relevant data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: A response containing the list of DictUser instances.
        """
        if request.user.is_superuser or request.user.dict_user.dict_admin:
            q = DictUser.objects.exclude(user=request.user.id)
            ser = self.get_serializer(q, many=True)
            return Response(ser.data)
        return Response('You do not have required permission')
    
    def retrieve(self, request, *args, **kwargs):    
        """
        Retrieve a DictUser instance.
        Only superusers and dict_admins can retrieve a DictUser instance.
        If the request user is not a superuser or dict_admin, a response with status code 403 and a message
        "You do not have required permission" is returned.
        Parameters:
            request (Request): The request containing the user and other relevant data.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: A response containing the DictUser instance.
        """
        if request.user.is_superuser or request.user.dict_user.dict_admin:
            return super().retrieve(request, *args, **kwargs)
        return Response('You do not have required permission')
    
    
class DiplomaticTermView(mixins.ListModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    # prefetch_related(
    #     'related_terms',
    #     'categories',
    #     'related_countries',
    #     'sources',
    #     'photo_id',
    # )
    serializer_class = DiplomaticTermReadSerializer

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        """
    List all DiplomaticTerm instances.
    This view caches the result for 5 minutes.
    Parameters:
        request (Request): The request containing the user and other relevant data.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        Response: A response containing the list of DiplomaticTerm instances.
    """
        return super().list(request, *args, **kwargs)


class DiplomaticTermDetailView(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    # prefetch_related(
    #     'related_terms',
    #     'categories',
    #     'related_countries',
    #     'sources',
    #     'photo_id',
    # )
    serializer_class = DiplomaticTermDetailSerializer


class SearchTermView(mixins.ListModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.all()
    serializer_class = DiplomaticTermReadSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title',]


class CreateDiplomaticTermView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = DiplomaticTerm.objects.prefetch_related(
        'related_terms',
        'categories',
        'related_countries',
        'sources',
        'photo_id',
    )

    serializer_class = DiplomaticTermWriteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):
        """
    List all DiplomaticTerm instances.
    This view caches the result for 5 minutes.
    Parameters:
        request (Request): The request containing the user and other relevant data.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        Response: A response containing the list of DiplomaticTerm instances.
    """
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = DiplomaticTermReadSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = DiplomaticTermReadSerializer(queryset, many=True)
        return Response(serializer.data)
    

    def retrieve(self, request, *args, **kwargs):
        """
    Retrieve a DiplomaticTerm instance.
    Parameters:
        request (Request): The request containing the user and other relevant data.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        Response: A response containing the DiplomaticTerm instance.
    """
        instance = self.get_object()
        ser = DiplomaticTermDetailSerializer(instance)
        return Response(ser.data)
    
    def create(self, request, *args, **kwargs):
        """
        Create a new DiplomaticTerm instance.
        Parameters:
            request (Request): The request containing the data for the new DiplomaticTerm instance.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: A response containing the data for the new DiplomaticTerm instance.
        """
        serializer = DiplomaticTermWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DiplomaticTermPhotoAdminView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = DiplomaticTermPhoto.objects.all()
    serializer_class = DiplomaticTermPhotoSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class DiplomaticTermPhotoView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = DiplomaticTermPhoto.objects.all()
    serializer_class = DiplomaticTermPhotoSerializer


class CountryAdminView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class CountryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SourceAdminView(mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class SourceView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateCategoryView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]


class UserCreateView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        """
    Create a new User instance.
    Parameters:
        request (Request): The request containing the data for the new User instance.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.
    Returns:
        Response: A response containing the data for the new User instance.
    Raises:
        ValidationError: If the input data is invalid.
    """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save(user_type='dict_user')
        res = self.get_serializer(user)
        return Response(res.data, status=status.HTTP_201_CREATED)


class ContactView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactAdminView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, BasicAuthentication]

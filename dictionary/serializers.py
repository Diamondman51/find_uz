from rest_framework import serializers

from dictionary.models import Category, Contact, Country, DiplomaticTerm, DiplomaticTermPhoto, Source


class DiplomaticTermPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTermPhoto
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']


class RelatedDiplomaticTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTerm
        fields = ['id', 'title', 'created_at', 'updated_at']  # only show basic info to avoid recursion


class DiplomaticTermReadSerializer(serializers.ModelSerializer):
    related_terms = RelatedDiplomaticTermSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    related_countries = CountrySerializer(many=True, read_only=True)
    sources = SourceSerializer(many=True, read_only=True)
    class Meta:
        model = DiplomaticTerm
        exclude = ['photo_id']
        # fields = '__all__'
        # extra_kwargs = {'title': {'required': True}, 
        #                 'definition': {'required': True}, 
        #                 'related_terms': {'required': False}, 
        #                 'categories': {'required': False}, 
        #                 'related_countries': {'required': False}, 
        #                 'sources': {'required': False}}



class DiplomaticTermWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTerm
        exclude = ['photo_id']
        # fields = '__all__'
        extra_kwargs = {'title': {'required': True}, 
                        'definition': {'required': True}, 
                        'related_terms': {'required': False}, 
                        'categories': {'required': False}, 
                        'related_countries': {'required': False}, 
                        'sources': {'required': False}}


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


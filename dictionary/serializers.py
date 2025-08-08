from rest_framework import serializers

from dictionary.models import Category, Country, DiplomaticTerm, DiplomaticTermPhoto, Source

class DiplomaticTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTerm
        fields = '__all__'
        extra_kwargs = {'title': {'required': True}, 
                        'definition': {'required': True}, 
                        'related_terms': {'required': False}, 
                        'category': {'required': False}, 
                        'related_countries': {'required': False}, 
                        'sources': {'required': False}}
        

class DiplomaticTermPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTermPhoto
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



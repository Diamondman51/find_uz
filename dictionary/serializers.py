from rest_framework import serializers

from dictionary.models import Category, Country, DiplomaticTerm, DiplomaticTermPhoto, Source


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
        fields = ['id', 'name']


class RelatedDiplomaticTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTerm
        fields = ['id', 'title']  # only show basic info to avoid recursion


class DiplomaticTermSerializer(serializers.ModelSerializer):
    photo_id = DiplomaticTermPhotoSerializer(many=True, read_only=True)
    sources = SourceSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    related_countries = CountrySerializer(many=True, read_only=True)
    # related_terms = RelatedDiplomaticTermSerializer(many=True, read_only=True)
    class Meta:
        model = DiplomaticTerm
        fields = '__all__'
        extra_kwargs = {'title': {'required': True}, 
                        'definition': {'required': True}, 
                        'related_terms': {'required': False}, 
                        'category': {'required': False}, 
                        'related_countries': {'required': False}, 
                        'sources': {'required': False}}
        depth = 1

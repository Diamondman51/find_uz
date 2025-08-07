from rest_framework import serializers

from dictionary.models import Category, DiplomaticTerm, DiplomaticTermPhoto

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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



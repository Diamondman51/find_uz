from rest_framework import serializers

from dictionary.models import Category, Country, DiplomaticTerm, Source


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name', 'iso_code', 'description', 'created_at', 'updated_at']


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'title', 'url', 'publication_date', 'created_at', 'updated_at']


class DiplomaticTermReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTerm
        fields = ['id', 'title', 'photo', 'created_at', 'updated_at']


class DiplomaticTermDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    related_countries = CountrySerializer(many=True, read_only=True)
    sources = SourceSerializer(many=True, read_only=True)
    related_terms = DiplomaticTermReadSerializer(many=True, read_only=True)

    class Meta:
        model = DiplomaticTerm
        fields = [
            'id', 'title', 'photo', 'definition',
            'category', 'related_countries', 'sources', 'related_terms',
            'created_at', 'updated_at',
        ]


class DiplomaticTermWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTerm
        fields = [
            'id', 'title', 'photo', 'definition',
            'category', 'related_countries', 'sources', 'related_terms',
        ]
        extra_kwargs = {
            'title': {'required': True},
            'definition': {'required': True},
            'related_terms': {'required': False},
            'category': {'required': False},
            'related_countries': {'required': False},
            'sources': {'required': False},
        }

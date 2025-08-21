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
    # related_terms = RelatedDiplomaticTermSerializer(many=True, read_only=True)
    # categories = CategorySerializer(many=True, read_only=True)
    # related_countries = CountrySerializer(many=True, read_only=True)
    # sources = SourceSerializer(many=True, read_only=True)
    class Meta:
        model = DiplomaticTerm
        # exclude = ['photo_id']
        fields = ['id', 'title']
        # extra_kwargs = {'title': {'required': True},
        #                 'definition': {'required': True},
        #                 'related_terms': {'required': False},
        #                 'categories': {'required': False},
        #                 'related_countries': {'required': False},
        #                 'sources': {'required': False}}


class DiplomaticTermDetailSerializer(serializers.ModelSerializer):
    related_terms = RelatedDiplomaticTermSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    related_countries = CountrySerializer(many=True, read_only=True)
    sources = SourceSerializer(many=True, read_only=True)
    class Meta:
        model = DiplomaticTerm
        exclude = ['photo_id']
        # fields = ['id', 'title']
        # extra_kwargs = {'title': {'required': True},
        #                 'definition': {'required': True},
        #                 'related_terms': {'required': False},
        #                 'categories': {'required': False},
        #                 'related_countries': {'required': False},
        #                 'sources': {'required': False}}



class DiplomaticTermWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiplomaticTerm
        # exclude = ['photo_id']
        fields = ['id', 'title', 'categories']
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


class DictUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(source='id', read_only=True)
    username = serializers.CharField(source='user.username')
    phone_number = serializers.CharField(source='user.phone_number')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    is_admin = serializers.BooleanField(source='dict_admin')
    password = serializers.CharField(source='user.password', write_only=True)

    # extra_kwargs = 

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()

        instance.dict_admin = validated_data.get("dict_admin", instance.dict_admin)
        instance.save()
        return instance

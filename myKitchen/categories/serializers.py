from rest_framework import serializers

from categories.models import Category, Categories_Defined

class CategoryField(serializers.RelatedField):

    def to_representation(self, value):
        return value

    def to_internal_value(self, value):
        return value

class DefinedCategoriesSerializer(serializers.ModelSerializer):
    category_id = CategoryField(queryset=Category.objects.values_list('name', flat=True))

    class Meta:
        model = Categories_Defined
        fields = ('name','description','category_id')

    def create(self, validated_data):
        category_id = validated_data['category_id']
        category = Category.objects.get(id=category_id)

        defined_category = Categories_Defined.objects.create(
            category=category,
            name=validated_data['name'],
            description=validated_data['description']
        )

        return defined_category

class CategorySerializer(serializers.ModelSerializer):
    defined_category_values = DefinedCategoriesSerializer(required=False, many=True)

    class Meta:
        model = Category
        fields = ('uuid','name','description','defined_category_values')

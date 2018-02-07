import json
from django.contrib.auth import get_user_model
from rest_framework import serializers

from recipes.serializers import RecipeSummarySerializer
from recipes.models import Recipe
from subscriptions.models import FeaturedRecipe, Likes, Views

class RecipeField(serializers.RelatedField):

        def to_representation(self, value):
            return value

        def to_internal_value(self, value):
            return value

class FeaturedRecipesListSerializer(serializers.ModelSerializer):
    featured_recipe = RecipeSummarySerializer(source='recipe_set', many=True)

    class Meta:
        model = FeaturedRecipe
        fields = ('featured_recipe',)

class FeaturedRecipesCreateSerializer(serializers.ModelSerializer):
    recipe = RecipeField(queryset=Recipe.objects.values_list('name', flat=True))

    class Meta:
        model = FeaturedRecipe
        fields = ('feature_type','recipe')

    def create(self, validated_data):
        feature_type = validated_data['feature_type']
        recipe = Recipe.objects.get(name=validated_data['recipe'])

        feature = FeaturedRecipe.objects.create(
            feature_type = feature_type,
            recipe = recipe
        )

        return feature

class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = '__all__'

class ViewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Views
        fields = '__all__'

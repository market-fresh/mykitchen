from django.contrib.auth import get_user_model
from rest_framework import serializers

from categories.models import Category
from recipes.models import Recipe, Step, Tag, Recipe_Category, Ingredients
from subscriptions.models import Likes, Views

class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ('step_id','name','description','photo')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('tags',)

class CategoryListSerializer(serializers.ModelSerializer):
    category_id = serializers.ReadOnlyField(source='category.id')
    name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Recipe_Category
        fields = ('category_id','name','value')

class CategoryField(serializers.RelatedField):

    def to_representation(self, value):
        return value.name

    def to_internal_value(self, value):
        return value.name

class CategorySerializer(serializers.ModelSerializer):
    category_name = CategoryField(queryset=Category.objects.values_list('name', flat=True))

    class Meta:
        model = Recipe_Category
        fields = ('category_name','value')
        #fields = '__all__'

class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ('name','price','quantity','measure')

class RecipeListSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(source='recipe_category_set', many=True)
    tags = TagSerializer(source='tag_set', many=True)
    view_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ('user','user_name','uuid','name','subheader','cover_photo','categories','tags','view_count','like_count')

    def get_view_count(self, obj):
        return Views.objects.count_recipe_views(obj)

    def get_like_count(self, obj):
        return Likes.objects.count_recipe_likes(obj)

    def get_user_name(self, obj):
        User = get_user_model()
        return User.objects.filter(username=obj.user).values('username')

class RecipeSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('uuid','name','cover_photo', 'created_date')

class RecipeCreateSerializer(serializers.ModelSerializer):
    steps = StepSerializer(required=False, many=True)
    ingredients = IngredientsSerializer(required=False, many=True)
    category = CategorySerializer(required=False, many=True)
    tags = TagSerializer(required=False, many=True)

    #steps = StepSerializer(required=False)
    #ingredients = IngredientsSerializer(required=False)
    #category = CategorySerializer(required=False)
    #tags = TagSerializer(required=False)

    class Meta:
        model = Recipe
        fields = ('user','name','subheader','story','cover_photo','video_link','status','steps','ingredients','category','tags')

    def create(self, validated_data):
        step_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')
        category_data = validated_data.pop('category')
        tag_data = validated_data.pop('tags')

        User = get_user_model()
        user = User.objects.get(username=validated_data.pop('user'))

        recipe = Recipe.objects.create(user=user, **validated_data)
        recipe.save()

        for step in step_data:
            Step.objects.create(recipe=recipe, **step)
        for ingredient in ingredients_data:
            Ingredients.objects.create(recipe=recipe, **ingredient)
        for category in category_data:
            Recipe_Category.objects.create(recipe=recipe, **category)
        for tag in tag_data:
            Tag.objects.create(recipe=recipe, **tag)

        #Step.objects.create(recipe=recipe, **step_data)
        #Ingredients.objects.create(recipe=recipe, **ingredients_data)
        #Recipe_Category.objects.create(recipe=recipe, **category_data)
        #Tag.objects.create(recipe=recipe, **tag_data)

        return recipe


class RecipeDetailsSerializer(serializers.ModelSerializer):
    steps = StepSerializer(source='step_set', many=True)
    ingredients = IngredientsSerializer(source='ingredients_set', many=True)
    categories = CategoryListSerializer(source='recipe_category_set', many=True)
    tags = TagSerializer(source='tag_set', many=True)
    view_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    #rating of current user
    #isFavorite of current user
    #comments

    class Meta:
        model = Recipe
        fields = ('user','name','subheader','story','cover_photo','video_link','status','steps','ingredients','categories','tags','view_count','like_count')

    def get_view_count(self, obj):
        return Views.objects.count_recipe_views(obj)

    def get_like_count(self, obj):
        return Likes.objects.count_recipe_likes(obj)

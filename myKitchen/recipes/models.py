from django.db import models
from django.conf import settings

# Create your models here.
from core.models import TimeStampedModel
from core.models import RECIPE_STATUS, COMMENT_TYPES, RECIPE_CONSTANT, COMMENT_CONSTANT, USER_CONSTANT
from core.models import Rating as CoreRatingModel

from categories.models import Category as Categories_Category

class Cookbook(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('user__id','name',)

class RecipeManager(models.Manager):

    def count_user_recipes(self, user):
        r = Recipe.objects.filter(user=user)
        return r.count()

class Recipe(TimeStampedModel):
    #cookbook = models.ForeignKey('Cookbook', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    subheader = models.TextField(blank=True)
    status = models.IntegerField(default=1, choices=RECIPE_STATUS)
    story = models.TextField(blank=True)
    cover_photo = models.ImageField(upload_to='recipes/images/', blank=True)
    video_link = models.URLField(blank=True)

    objects = RecipeManager()

    class Meta:
        ordering = ('id',)

class Step(TimeStampedModel):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    step_id = models.IntegerField()
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')
    photo = models.ImageField(blank=True)
    video_link = models.URLField(blank=True)

    class Meta:
        ordering = ('recipe__id','step_id',)

class Ingredients(TimeStampedModel):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    #ingredients = models.ForeignKey('stores.Ingredients', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    measure = models.CharField(max_length=10, blank=True, default='')

    class Meta:
        ordering = ('recipe__id','name',)

class CategoryManager(models.Manager):

    def create(self, recipe, **validated_data):
        category_name = validated_data['category_name']
        category = Categories_Category.objects.get(name=category_name)
        return super().create(
            recipe=recipe,
            category=category,
            value=validated_data['value']
        )

class Recipe_Category(TimeStampedModel):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)#, related_name='recipe_categories')
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    objects = CategoryManager()

    class Meta:
        ordering = ('recipe__id','category__id',)

class Tag(TimeStampedModel):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    tags = models.CharField(max_length=150, blank=True, default='')

    class Meta:
        ordering = ('recipe__id','id',)

class Rating(CoreRatingModel):
    recipe = models.OneToOneField('Recipe', on_delete=models.CASCADE, related_name='recipe_rating')

class Comment(TimeStampedModel):
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    parent_type = models.CharField(max_length=2, choices=COMMENT_TYPES)
    parent_recipe = models.OneToOneField('Recipe', null=True, blank=True, on_delete=models.CASCADE)
    parent_comment = models.OneToOneField('Comment', null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    parent_user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='+')
    comments = models.TextField()

    class Meta:
        ordering = ('user__id','created_date',)

    @property
    def parent(self):
        if parent_type == RECIPE_CONSTANT:
            return parent_recipe
        elif parent_type == COMMENT_CONSTANT:
            return parent_comment
        elif parent_type == USER_CONSTANT:
            return parent_user
        else:
            raise AssertionError('This comment is not tied to a parent.')

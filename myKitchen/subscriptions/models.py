from django.db import models
from django.conf import settings

# Create your models here.
from core.models import TimeStampedModel
from core.models import RECIPE_CONSTANT, COOKBOOK_CONSTANT, COMMENT_CONSTANT, USER_CONSTANT, PARENT_TYPES

class ViewsManager(models.Manager):

    def count_recipe_views(self, recipe):
        v = Views.objects.filter(recipe=recipe)
        return v.count()

    def list_user_views(self, user):
        return Views.objects.filter(user=user)


class Views(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    objects = ViewsManager()

    class Meta:
        ordering = ('user__id','recipe__id','created_date',)

class LikesManager(models.Manager):

    def count_recipe_likes(self, input_recipe):
        l = Likes.objects.filter(recipe=input_recipe)
        return l.count()

    def list_user_likes(self, input_user):
        return Likes.objects.filter(user=input_user)

class Likes(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    objects = LikesManager()

    class Meta:
        ordering = ('user__id','recipe__id','created_date',)

class FeaturedRecipe(TimeStampedModel):
    feature_type = models.CharField(max_length=2, choices=PARENT_TYPES)
    recipe = models.OneToOneField('recipes.Recipe', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id','created_date',)

class FeaturedUser(TimeStampedModel):
    feature_type = models.CharField(max_length=2, choices=PARENT_TYPES)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id','created_date',)


class Favorites(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_type = models.CharField(max_length=2, choices=PARENT_TYPES)
    parent_recipe = models.OneToOneField('recipes.Recipe', null=True, blank=True, on_delete=models.CASCADE)
    parent_cookbook = models.OneToOneField('recipes.Cookbook', null=True, blank=True, on_delete=models.CASCADE)
    parent_user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    class Meta:
        ordering = ('user__id','created_date',)

    @property
    def parent(self):
        if parent_type == RECIPE_CONSTANT:
            return parent_recipe
        elif parent_type == COOKBOOK_CONSTANT:
            return parent_cookbook
        elif parent_type == USER_CONSTANT:
            return parent_user
        else:
            raise AssertionError('This favorite is not tied to a parent.')

class Follows(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_type = models.CharField(max_length=2, choices=PARENT_TYPES)
    parent_recipe = models.OneToOneField('recipes.Recipe', null=True, blank=True, on_delete=models.CASCADE)
    parent_cookbook = models.OneToOneField('recipes.Cookbook', null=True, blank=True, on_delete=models.CASCADE)
    parent_user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='+')

    class Meta:
        ordering = ('user__id','created_date',)

    @property
    def parent(self):
        if parent_type == RECIPE_CONSTANT:
            return parent_recipe
        elif parent_type == COOKBOOK_CONSTANT:
            return parent_cookbook
        elif parent_type == USER_CONSTANT:
            return parent_user
        else:
            raise AssertionError('This follow is not tied to a parent.')

from django.contrib.auth import get_user_model
from rest_framework import serializers

from cart.models import Item, Cart
from recipes.models import Recipe

class RecipeField(serializers.RelatedField):

    def to_representation(self, value):
        return value

    def to_internal_value(self, value):
        return value

class ItemSerializer(serializers.ModelSerializer):
    recipe_id = RecipeField(queryset=Recipe.objects.values_list('id', flat=True))
    recipe_name = RecipeField(queryset=Recipe.objects.values_list('name', flat=True))

    class Meta:
        model = Item
        fields = ('recipe_name','recipe_id', 'name', 'description', 'price', 'quantity', 'measure')

class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(required=False, many=True)

    class Meta:
        model = Cart
        fields = ('user', 'items')

    def create(self, validated_data):
        item_data = validated_data.pop('items')

        User = get_user_model()
        user = User.objects.get(username=validated_data.pop('user'))

        cart = Cart.objects.create(user=user, **validated_data)
        cart.save()

        for item in item_data:
            Item.objects.create(cart=cart, **step)

        return cart

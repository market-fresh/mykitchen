from rest_framework import serializers

from stores.models import Store, Ingredients

class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ('collection','name','description','price','quantity','measure')

class StoreSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer(required=False, many=True)

    class Meta:
        model = Store
        fields = ('name','description','ingredients')

    def create(self, validated_data):
        ingredients_data = validated_data.pop('items')

        store = Store.objects.create(**validated_data)
        store.save()

        for ingredient in ingredients_data:
            Ingredients.objects.create(store=store, **ingredient)

        return store

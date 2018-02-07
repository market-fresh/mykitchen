from django.test import TestCase

# Create your tests here.
from .models import Store, Ingredients

class Stores_Test(TestCase):
    """ Test module for Store model """

    def setUp(self):
        store_mf = Store.objects.create(
            name='Market Fresh',
            description='Market Fresh'
        )
        Store.objects.create(
            name='The Bake Shoppe',
            description='The Bake Shoppe'
        )

        Ingredients.objects.create(
            collection_type='Poultry',
            name='Chicken Breast',
            description='Chicken Breast',
            price=4.99,
            quantity=500,
            measure='grams',
            store=store_mf
        )

    def test_store(self):
        store_mf = Store.objects.get(name='Market Fresh')
        store_bs = Store.objects.get(name='The Bake Shoppe')

        self.assertEqual(
            store_mf.description,'Market Fresh'
        )

        self.assertEqual(
            store_bs.description,'The Bake Shoppe'
        )

    def test_ingredients(self):
        store_mf = Store.objects.get(name='Market Fresh')
        ingredients_mf = Ingredients.objects.get(store=store_mf, name='Chicken Breast')

        self.assertEqual(
            ingredients_mf.price,4.99
        )

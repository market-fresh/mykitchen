from django.test import TestCase

# Create your tests here.
from .models import Category, Categories_Defined
from . import util

class Categories_Test(TestCase):
    """ Test module for Category model """

    def setUp(self):
        method = Category.objects.create(
            name='Method',
            description='Describes the method of cooking for the recipe.'
        )
        prep_time = Category.objects.create(
            name='Preparation Time',
            description='Describes the length of time to prepare the recipe.'
        )

        serving = Category.objects.create(
            name='Serving',
            description='Describes the number of people the recipe can serve.'
        )

        country_of_origin = Category.objects.create(
            name='Country of Origin',
            description='Describes the origin of the recipe.'
        )

        difficulty = Category.objects.create(
            name='Difficulty',
            description='Describes the difficulty in preparing the recipe.'
        )

        list_of_countries = util.get_list_of_countries()
        i = 1

        for country in list_of_countries:
            Categories_Defined.objects.create(
                name = list_of_countries[country],
                description = country,
                category = country_of_origin
            )
            i = i + 1

    def test_category(self):
        country_of_origin = Category.objects.get(name='Country of Origin')
        difficulty = Category.objects.get(name='Difficulty')

        self.assertEqual(
            country_of_origin.name,'Country of Origin'
        )

        self.assertEqual(
            difficulty.description,'Describes the difficulty in preparing the recipe.'
        )

    def test_category_defined(self):
        country_of_origin = Category.objects.get(name='Country of Origin')
        sg = Categories_Defined.objects.get(category=country_of_origin, description='SG')

        self.assertEqual(
            sg.name, 'Singapore'
        )

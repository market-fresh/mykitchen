from django.db import models

# Create your models here.
from core.models import TimeStampedModel

class Store(TimeStampedModel):
    """ Store Model """
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

class Ingredients(TimeStampedModel):
    """ Ingredients Model """
    store = models.ForeignKey('Store', on_delete=models.CASCADE)
    collection = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')
    price = models.FloatField()
    quantity = models.IntegerField()
    measure = models.CharField(max_length=10, blank=True, default='')
    photo = models.ImageField()

    class Meta:
        ordering = ('store__id','name',)

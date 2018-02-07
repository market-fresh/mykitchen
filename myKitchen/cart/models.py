from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
from core.models import TimeStampedModel

class Cart(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def get_absolute_url(self):
        return reverse('cart:detail', kwargs={'slug': self.slug})

class Item(TimeStampedModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    recipe = models.ForeignKey('recipes.Recipe')
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')
    price = models.FloatField()
    quantity = models.IntegerField()
    measure = models.CharField(max_length=10, blank=True, default='')

    class Meta:
        ordering = ('id','recipe__id','name',)

    def get_absolute_url(self):
        return reverse('item:detail', kwargs={'slug': self.slug})

class Purchased(TimeStampedModel):
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    class Meta:
        ordering = ('user__id','recipe__id','created_date',)

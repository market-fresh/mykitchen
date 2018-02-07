from django.db import models
from django.conf import settings

# Create your models here.
from core.models import TimeStampedModel

class Purse(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    purchased = models.ForeignKey('cart.Purchased', on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        ordering = ('user__id','created_date',)

class Points(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    purchased = models.ForeignKey('cart.Purchased', on_delete=models.CASCADE)
    amount = models.FloatField()

    class Meta:
        ordering = ('user__id','created_date',)

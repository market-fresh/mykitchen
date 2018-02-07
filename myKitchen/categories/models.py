from django.db import models

# Create your models here.
from core.models import TimeStampedModel

class Category(TimeStampedModel):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('category:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.name


class Categories_Defined(TimeStampedModel):
    category = models.ForeignKey('Category', related_name='defined_category_values')
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('category__id','name',)

    def __unicode__(self):
        return '%s: %s' % ('uuid','name')

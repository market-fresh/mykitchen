from django.db import models
from django.conf import settings
import uuid as uuidlib

# Create your models here.
from django.utils import timezone

RECIPE_CONSTANT = 'RE'
COOKBOOK_CONSTANT = 'CB'
COMMENT_CONSTANT = 'CO'
USER_CONSTANT = 'US'

PARENT_TYPES = (
    (RECIPE_CONSTANT,'Recipe'),
    (COOKBOOK_CONSTANT,'Cookbook'),
    (USER_CONSTANT,'User')
)

COMMENT_TYPES = (
    ('R','Recipe'),
    ('C','Comment'),
    ('U','User')
)

RATING_TYPES = (
    ('1','Rating'),
    ('2','Review')
)

RECIPE_STATUS = (
    ('1','Draft'),
    ('2','For Vetting'),
    ('3','Published')
)

ADDRESS_TYPE = (
    ('1','Billing'),
    ('2','Shipping'),
)

class TimeStampedModelManager(models.Manager):

    def save(self, **kwargs):
        kwargs['updated_date'] = timezone.now()
        return super().save(**kwargs)

class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

#    slug = models.SlugField(unique=True)
    uuid = models.UUIDField(db_index=True, default=uuidlib.uuid4, editable=False)

    objects = TimeStampedModelManager()

    class Meta:
        abstract = True

class Rating(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    purchased = models.ForeignKey('cart.Purchased', on_delete=models.CASCADE, related_name='+')
    rating_type = models.CharField(max_length=1, choices=RATING_TYPES)
    stars = models.IntegerField(null=True, blank=True)
    review = models.TextField()

    class Meta:
        abstract = True
        ordering = ('user__id','created_date',)

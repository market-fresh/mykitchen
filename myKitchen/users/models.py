from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
from core.models import TimeStampedModel
from core.models import Rating as CoreRatingModel
from core.models import ADDRESS_TYPE

class UserManager(models.Manager):
    User = get_user_model()

    def unatural_key(self):
        return self.username
    User.natural_key = unatural_key

class Address(TimeStampedModel):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    address_type = models.CharField(max_length=1, choices=ADDRESS_TYPE)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, default='Singapore')
    city  = models.CharField(max_length=50, default='Singapore')
    unit_no = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=6)
    contact_no = models.CharField(max_length=15, blank=True)

class Profile(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='users/images/', blank=True)
    country = models.CharField(max_length=50, blank=True, default='Singapore')
    biography = models.TextField(blank=True)

    class Meta:
        ordering = ('id',)

class Rating(CoreRatingModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_rating')

class Settings_Group(TimeStampedModel):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ('id','name',)

class Settings(TimeStampedModel):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50, blank=True, default='')
    settings_group = models.ForeignKey('Settings_Group', on_delete=models.CASCADE)

    class Meta:
        ordering = ('settings_group__id','id','name',)

class User_Settings(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    settings = models.ForeignKey('Settings', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)

    class Meta:
        ordering = ('user__id','settings__id','id',)

class Social_Media(TimeStampedModel):
    social_media_type = models.CharField(max_length=50, blank=True, default='')
    authentication = models.TextField(max_length=50, blank=True, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('user__id','social_media_type',)

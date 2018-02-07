from rewards.models import Purse, Points
from rest_framework import serializers

from users.serializers import User_Serializer
from cart.serializers import Purchased_Serializer

class Purse_Serializer(serializers.ModelSerializer):
    user = User_Serializer()
    purchased = Purchased_Serializer()

    class Meta:
        model = Purse
        fields = ('user','purchased','amount')

class Points_Serializer(serializers.ModelSerializer):
    user = User_Serializer()
    purchased = Purchased_Serializer()

    class Meta:
        model = Points
        fields = ('user','purchased','amount')

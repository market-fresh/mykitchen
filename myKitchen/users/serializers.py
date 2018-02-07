from django.contrib.auth import get_user_model
from rest_framework import serializers

from recipes.models import Recipe
from users.models import Address, Profile

from recipes.serializers import RecipeSummarySerializer

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('address_type','address_1','address_2','unit_no','city','country','postal_code','contact_no')

class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer(source='address_set', many=True)

    class Meta:
        model = Profile
        fields = ('uuid','photo','country','biography','address')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = get_user_model()
        fields = ('pk','username','password','first_name','last_name','email','profile')

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create(
            username = validated_data['username'],
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )
        user.save()

        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user = user,
            photo = profile_data['photo'],
            country = profile_data['country'],
            biography = profile_data['biography']
        )
        profile.save()

        address_data = profile_data.pop('address')
        address = Address.objects.create(
            profile = profile,
            address_type  = address_data['address_type'],
            address_1 = address_data['address_1'],
            address_2 = address_data['address_2'],
            country = address_data['country'],
            city  = address_data['city'],
            unit_no = address_data['unit_no'],
            postal_code = address_data['postal_code'],
            contact_no = address_data['contact_no']
        )
        address.save()

        return user

    def update(self, user, validated_data):
        user.username = validated_data['username']
        user.password = validated_data['password']
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.save()

        profile, created = Profile.objects.get_or_create(user=user)
        profile_data = validated_data.pop('profile')

        profile.photo = profile_data['photo']
        profile.country = profile_data['country']
        profile.biography = profile_data['biography']
        profile.save()

        return user

class ProfileAboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('photo','biography')

class UserAboutMeSerializer(serializers.ModelSerializer):
    profile = ProfileAboutMeSerializer()
    recipe_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('username','profile','first_name','last_name','date_joined','recipe_count')

    def get_recipe_count(self, obj):
        return Recipe.objects.count_user_recipes(obj)

class ProfileAddressSerializer(serializers.ModelSerializer):
    address = AddressSerializer(source='address_set', many=True)

    class Meta:
        model = Profile
        fields = ('uuid','address')

class UserAddressSerializer(serializers.ModelSerializer):
    profile = ProfileAddressSerializer()

    class Meta:
        model = get_user_model()
        fields = ('pk','username','first_name','last_name','profile')

class UserMyRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSummarySerializer(source='recipe_set', many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk','username','first_name','last_name','recipe')

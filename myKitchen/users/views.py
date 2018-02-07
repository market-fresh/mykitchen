from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import Address, Profile
from users.serializers import UserSerializer, ProfileSerializer, UserAboutMeSerializer, UserAddressSerializer, UserMyRecipeSerializer

class UserListView(ListCreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    lookup_fields = 'pk'

#class UserAboutMeView(LoginRequiredMixin, RetrieveAPIView):
class UserAboutMeView(RetrieveAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = UserAboutMeSerializer
    lookup_fields = 'pk'

class UserAddressView(RetrieveAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = UserAddressSerializer
    lookup_fields = 'pk'

class UserMyRecipeView(RetrieveAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = UserMyRecipeSerializer
    lookup_fields = 'pk'

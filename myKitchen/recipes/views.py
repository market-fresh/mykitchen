from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from recipes.models import Recipe
from recipes.serializers import RecipeListSerializer, RecipeCreateSerializer, RecipeDetailsSerializer
from recipes.serializers import CategorySerializer

class RecipeListView(ListAPIView):
    """ List all recipes """
    template_name = 'index.html'
    #permission_classes = (IsAuthenticated, )
    serializer_class = RecipeListSerializer
    #lookup_field = 'username'

    def get_queryset(self):
        queryset = Recipe.objects.all()
        user_name = self.request.query_params.get('user',None)
        search = self.request.query_params.get('search',None)

        if user_name is not None:
            User = get_user_model()
            user = User.objects.get(username=user_name)
            if user is not None:
                return Recipe.objects.filter(user=user)

        elif search is not None:
            return queryset

        return queryset

class RecipeCreateView(CreateAPIView):
    """ List the details of a specific recipe """

    queryset = Recipe.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = RecipeCreateSerializer
    lookup_field = 'uuid'

class RecipeDetailView(RetrieveUpdateDestroyAPIView):
    """ List the details of a specific recipe """

    queryset = Recipe.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = RecipeDetailsSerializer
    lookup_field = 'uuid'

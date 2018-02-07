from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from recipes.models import Recipe
from recipes.serializers import RecipeSummarySerializer
from subscriptions.models import FeaturedRecipe, Likes, Views
from subscriptions.serializers import FeaturedRecipesListSerializer, FeaturedRecipesCreateSerializer, LikesSerializer, ViewsSerializer

# Create your views here.
class FeaturedRecipesListView(ListAPIView):
    #permission_classes = (IsAuthenticated, )
    serializer_class = RecipeSummarySerializer

    def get_queryset(self):
        featuredrecipe = FeaturedRecipe.objects.all()
        queryset = Recipe.objects.filter(id__contains=featuredrecipe)

        return queryset

class FeaturedRecipesCreateView(CreateAPIView):
    queryset = FeaturedRecipe.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = FeaturedRecipesCreateSerializer

class LikesView(ListCreateAPIView):
    queryset = Likes.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = LikesSerializer

class LikesDetailView(RetrieveUpdateDestroyAPIView):
#class LikesDetailView(DestroyAPIView):
    queryset = Likes.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = LikesSerializer
    lookup_field = 'uuid'

class ViewsView(ListCreateAPIView):
    queryset = Views.objects.all()
    serializer_class = ViewsSerializer

class ViewsDetailView(RetrieveUpdateDestroyAPIView):
#class ViewsDetailView(DestroyAPIView):
    queryset = Views.objects.all()
    serializer_class = ViewsSerializer
    lookup_field = 'uuid'

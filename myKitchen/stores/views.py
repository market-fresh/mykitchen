from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from stores.models import Store, Ingredients
from stores.serializers import StoreSerializer, IngredientsSerializer

class StoreListView(ListCreateAPIView):
    queryset = Store.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = StoreSerializer
    #lookup_field = 'uuid'

class StoreDetailedView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = StoreSerializer
    lookup_field = 'uuid'

class IngredientsListView(ListCreateAPIView):
    queryset = Ingredients.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = IngredientsSerializer
    #lookup_field = 'uuid'

class IngredientsDetailedView(RetrieveUpdateDestroyAPIView):
    queryset = Ingredients.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = IngredientsSerializer
    lookup_field = 'uuid'

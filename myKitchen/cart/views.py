from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from cart.models import Cart, Item
from cart.serializers import ItemSerializer, CartSerializer

class CartListView(ListCreateAPIView):
    queryset = Cart.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer
    #lookup_field = 'uuid'

class CartDetailedView(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer
    lookup_field = 'uuid'

class ItemListView(ListCreateAPIView):
    queryset = Item.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = ItemSerializer
    #lookup_field = 'uuid'

class ItemDetailedView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = ItemSerializer
    lookup_field = 'uuid'

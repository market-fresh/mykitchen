from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from categories.models import Category, Categories_Defined
from categories.serializers import CategorySerializer, DefinedCategoriesSerializer

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer
    lookup_field = 'uuid'


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = CategorySerializer
    lookup_field = 'uuid'

class DefinedCategoryListView(ListCreateAPIView):
    queryset = Categories_Defined.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = DefinedCategoriesSerializer
    #lookup_field = 'uuid'


class DefinedCategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Categories_Defined.objects.all()
    #permission_classes = (IsAuthenticated, )
    serializer_class = DefinedCategoriesSerializer
    lookup_field = 'uuid'

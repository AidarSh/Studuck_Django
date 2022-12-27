from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from . import models
from .models import University
from .serializers import UniversitySerializer, UniversityOneSerializer
from .service import ProductFilter

class UniversityListView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = ProductFilter
    ordering_fields = ('id', 'rating')
    search_fields = ['name', 'fullname']

class Product(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = University.objects.all()
    serializer_class = UniversityOneSerializer

from django.shortcuts import render
from core.models import Category
from rest_framework import generics

from .serializers import CategorySerializer


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)
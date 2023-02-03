from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from core.models import *
from .serializers import *

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BannerList(generics.ListAPIView):
    queryset = Banner.objects.get_object_or_404()
    serializer_class = BannerSerializer


class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ItemsDomainList(generics.ListCreateAPIView):
    queryset = ItemsDomain.objects.all()
    serializer_class = ItemsDomainSerializer

class ItemsDomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemsDomain.objects.all()
    serializer_class = ItemsDomainSerializer


class DomainList(generics.ListCreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class DomainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class OrderDomainListCreateAPIView(generics.ListCreateAPIView):
    queryset = OrderDomain.objects.all()
    serializer_class = OrderDomainSerializer


class OrderDomainRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDomain.objects.all()
    serializer_class = OrderDomainSerializer



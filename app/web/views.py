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


class BannerDetail(generics.RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Banner, pk=pk)

class AboutList(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class SubAboutList(generics.ListAPIView):
    queryset = SubAbout.objects.all()
    serializer_class = SubAboutSerializer


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



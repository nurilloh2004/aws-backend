from rest_framework import serializers
from core.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent_category', 'title', 'slug', 'is_active', 'date_created')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class SubAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAbout
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class ItemsDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsDomain
        fields = '__all__'


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'


class OrderDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDomain
        fields = ('id', 'user', 'name', 'type')
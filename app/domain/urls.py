from django.urls import path
from .views import CategoryListView, CategoryView
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/', CategoryView.as_view(), name='category'),
]
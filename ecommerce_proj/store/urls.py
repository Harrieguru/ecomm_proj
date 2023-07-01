from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('products/add/', views.add_product, name='add_product'),
    path('profile/', views.profile, name='profile'),
]
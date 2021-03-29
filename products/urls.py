from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='products'),
    path('<int:prod_id>/detail', views.product, name='product'),
    path('search', views.search, name='search'),
]

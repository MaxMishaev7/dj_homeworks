from django.urls import path
from .views import product_list
from .views import ProductDetails

urlpatterns = [
    path('product-all/', product_list, name='product-all'),
    path('product-detail/<int:product_id>/', ProductDetails.as_view(), name='product-detail'),
]